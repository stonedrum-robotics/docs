# Source setup

These instructions use the public SDK source rather than assuming a published package registry entry.

```bash
git clone https://github.com/stonedrum-robotics/dexterous-hand-sdk.git
cd dexterous-hand-sdk
git checkout 17d8768affe743e9f997f1df5b100ea782ee5526
```

From that directory, the small mock example can import the root package through `PYTHONPATH=.`; see [first movement](first-movement.md). It does not need a device or a ROS installation.

## Environment evidence

The project declares Python `>=3.10`. Recorded local checks cover Python 3.11 and 3.12; that evidence does not establish a tested operating-system matrix or a Python 3.10 pass. The correction PR's hosted CI ran Ruff, mypy and pytest on Python 3.11.

For SDK development, use a virtual environment and the dependencies declared in `pyproject.toml`; `python -m pip install -e ".[dev]"` installs those dependencies. The editable-install path and downloaded dependency set need their own environment-specific validation. The mock examples use standard-library source interfaces; no package launch or dependency cleanup is implied.

ROS 2 and Docker have [separate source status](../ros2-integration/overview.md). They are not prerequisites for the Python mock and are not verified by its tests.
