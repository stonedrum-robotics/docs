# Launch file source status

The repository installs `launch/hand.launch.py`. It creates one `hand_node` process named `dexterous_hand` and declares a launch argument named `mock` with default `true`.

## Important distinction

The node parameters in this file contain the literal `{"mock": True}`; the launch argument is not wired through `LaunchConfiguration`. Separately, `HandNode` directly constructs `Hand.mock()` and does not read a backend parameter. Setting `mock:=false` does not turn this source into a hardware driver.

`config/default.yaml` contains mock, publishing-rate and joint-name values, but the inspected launch file does not load that YAML file and the node does not declare/read those parameters. Do not infer a configurable runtime from installed files alone.

This page replaces the former hardware-launch recipe with an explanation of actual source behavior. A working ROS launch/build environment and any future configuration changes require separate validation; none were executed during this documentation repair.
