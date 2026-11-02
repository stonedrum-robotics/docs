"""Check built routes, local link targets/anchors and generated Python API output."""
import argparse
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup


def check(site: Path, source: Path) -> dict:
    errors = []
    routes = []
    parsed = {}

    def html(path):
        path = path.resolve()
        if path not in parsed:
            parsed[path] = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        return parsed[path]

    for page in sorted(source.rglob("*.md")):
        relative = page.relative_to(source)
        target = site / "index.html" if str(relative) == "index.md" else site / relative.with_suffix("") / "index.html"
        routes.append(str(relative))
        if not target.is_file():
            errors.append({"source": str(relative), "error": "missing rendered page"})
    if len(routes) != 44:
        errors.append({"error": "expected 44 document routes", "actual": len(routes)})
    for page in sorted(site.rglob("*.html")):
        for element in html(page).select("[href], [src]"):
            reference = element.get("href") if element.has_attr("href") else element.get("src")
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            target = site / path.removeprefix("/docs/").lstrip("/") if path.startswith("/") else page.parent / path
            if not path:
                target = page
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append({"page": str(page.relative_to(site)), "link": reference, "error": "missing local target"})
                continue
            if url.fragment and target.suffix == ".html":
                fragment = unquote(url.fragment)
                if not html(target).find(id=fragment) and not html(target).find("a", attrs={"name": fragment}):
                    errors.append({"page": str(page.relative_to(site)), "link": reference, "error": "missing anchor"})
    api = {"hand": "Hand", "finger": "validate_positions", "driver": "MockHandDriver",
           "grasp-library": "GraspLibrary", "teleoperation": "TeleoperationController"}
    for page, symbol in api.items():
        target = site / "api-reference" / page / "index.html"
        if target.is_file():
            text = html(target).select_one("article").get_text(" ", strip=True)
            if symbol not in text or "::: dexterous_hand" in text:
                errors.append({"page": str(target.relative_to(site)), "error": "API content not generated"})
    return {"route_count": len(routes), "routes": routes, "api_pages": list(api), "errors": errors,
            "external_links": "not checked by this structural check"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    result = check(arguments.site.resolve(), arguments.source.resolve())
    arguments.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{result['route_count']} routes, {len(result['api_pages'])} API pages, {len(result['errors'])} link/render errors")
    raise SystemExit(bool(result["errors"]))
