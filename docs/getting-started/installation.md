# Installation

The SDK can be installed directly via pip. We recommend using a virtual environment.

```bash
# Create and activate a virtual environment
python3 -m venv dexenv
source dexenv/bin/activate

# Install the SDK
pip install dexterous-hand
```

## ROS 2 Setup

If you are using ROS 2, clone the repository into your workspace and build it:

```bash
cd ~/ros2_ws/src
git clone https://github.com/stonedrum-robotics/dexterous-hand-sdk.git
cd ~/ros2_ws
colcon build --packages-select dexterous_hand_ros2
source install/setup.bash
```

## Docker Option

A `docker-compose.yml` file is provided for quick setup. See the [Docker Deployment](../deployment/docker.md) guide.
