# Installation

This guide covers everything you need to install the Dexterous Hand SDK and integrate it into your development environment.

## Prerequisites

Before installing the SDK, ensure your system meets the following requirements:

*   **Operating System:** Ubuntu 22.04 LTS or Ubuntu 24.04 LTS.
*   **Python:** Python 3.10 or higher.
*   **ROS2 (Optionnel but Recommended):** ROS2 Humble Hawksbill (for Ubuntu 22.04) or ROS2 Jazzy Jalisco (for Ubuntu 24.04).

## Standard Python Installation

If you simply want to use the SDK without modifying its source code, you can install it directly via `pip`.

```bash
pip install dexterous-hand
```

*Expected Output:*
```text
Successfully installed dexterous-hand-x.y.z
```

## Development Installation

If you plan to contribute to the SDK or need to modify its core behavior, we recommend an editable installation. This allows you to change the code and see the effects immediately without reinstalling.

1.  Clone the repository:
    ```bash
    git clone https://github.com/stonedrum-robotics/dexterous-hand-sdk.git
    cd dexterous-hand-sdk
    ```
2.  Install in editable mode with development dependencies:
    ```bash
    pip install -e ".[dev]"
    ```

## ROS2 Workspace Setup

To use the SDK within a ROS2 environment, you need to build it as part of your colcon workspace.

1.  Navigate to your ROS2 workspace's `src` directory:
    ```bash
    cd ~/ros2_ws/src
    ```
2.  Clone the repository:
    ```bash
    git clone https://github.com/stonedrum-robotics/dexterous-hand-sdk.git
    ```
3.  Build the workspace:
    ```bash
    cd ~/ros2_ws
    colcon build --packages-select dexterous_hand
    ```
4.  Source the overlay:
    ```bash
    source install/setup.bash
    ```

## Docker Installation

For an isolated environment, we provide a Docker image based on `ros:humble-ros-base`. It includes Python, colcon, and a pre-installed editable version of the SDK.

1.  Navigate to the SDK directory:
    ```bash
    cd dexterous-hand-sdk
    ```
2.  Build the Docker image using the provided `docker/Dockerfile`:
    ```bash
    docker build -t dexterous-hand-sdk -f docker/Dockerfile .
    ```
3.  Run the container:
    ```bash
    docker run -it dexterous-hand-sdk
    ```

## Verify Installation

To confirm the SDK is installed correctly, run a quick test using the mock interface:

```bash
python -c "from dexterous_hand import Hand; print(Hand.mock())"
```

*Expected Output:*
```text
<dexterous_hand.hand.Hand object at 0x...>
```

## Troubleshooting Common Errors

**Error:** `ModuleNotFoundError: No module named 'dexterous_hand'`
*   **Fix:** Ensure you have activated the correct Python virtual environment or sourced your ROS2 workspace (`source install/setup.bash`) where the SDK was installed.

**Error:** `colcon: command not found`
*   **Fix:** If you are building the ROS2 package, you need to install the `python3-colcon-common-extensions` package via `apt`. Run `sudo apt install python3-colcon-common-extensions`.

**Error:** Permission denied when accessing USB/CAN devices.
*   **Fix:** Add your user to the `dialout` group: `sudo usermod -a -G dialout $USER`, then log out and log back in.

Need further assistance? Contact Stonedrum Robotics support at info@stonedrum.co.
