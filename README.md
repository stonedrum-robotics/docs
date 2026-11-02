# Documentation Portal

MkDocs Material source for the Stonedrum Robotics public SDK reference. API pages render from a fixed public SDK commit, separately checked out beside this repository.

## Local build

With Python3.11, use this sibling layout:

```bash
mkdir stonedrum-docs
cd stonedrum-docs
git clone https://github.com/stonedrum-robotics/docs.git docs-source
git clone https://github.com/stonedrum-robotics/dexterous-hand-sdk.git sdk-source
git -C sdk-source checkout 17d8768affe743e9f997f1df5b100ea782ee5526
python3.11 -m venv .venv
.venv/bin/python -m pip install --requirement docs-source/requirements-docs.txt
cd docs-source
../.venv/bin/python -m mkdocs build --strict --site-dir site
../.venv/bin/python tools/check_docs.py --site site --source docs --output checks.json
```

Preview locally from `docs-source` with `../.venv/bin/python -m mkdocs serve --dev-addr 127.0.0.1:8000`.

## Publication

The static output is the build artifact in `site/`. Publication is a separate operation from source preparation: verify all44 routes and API pages, retain the previous artifact commit in Git history, and publish by an ordinary fast-forward commit/push to the deployment branch. Do not use a force deployment or rewrite that branch's history. No package release or SDK tag is needed for a documentation publication.
