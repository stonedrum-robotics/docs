# ROS 2 source overview

The SDK repository includes `ros2_ws/src/dexterous_hand_ros2/`. This is integration source with a different verification boundary from the standalone Python mock. No Humble/Iron/Jazzy compatibility matrix or physical-device support is established by the mock tests.

## What is present

- `HandNode` constructs `Hand.mock()` and publishes software `JointState` messages from a timer.
- `TeleoperationNode` and `GraspActionServer` start nodes and log messages; they do not implement the documented live command/action pipelines.
- `setup.py` declares three console entry points and installs a launch file and configuration file.

The [nodes](nodes.md), [interfaces](topics-services.md) and [launch file](launch-files.md) pages describe these exact source boundaries. This repair statically checked those files; it did not run a ROS graph, build with colcon or verify a ROS environment.

Start with the [Python mock](../getting-started/first-movement.md) when exploring joint-state objects. A future ROS runtime evaluation needs its own pinned environment, build/run evidence and interface checks.
