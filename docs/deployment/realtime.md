# Timing and performance scope

The current reference mock stores values in a dictionary; it is not a real-time controller. A ROS source timer period or requested loop frequency is not a measured end-to-end latency, deadline or hardware control rate.

## Define a measurement before tuning

For a future timing experiment, identify the hardware/software versions, input/output points, clock/timestamp conventions, workload and error/deadline measure. Report observed distributions and conditions rather than inferring performance from a configuration value.

No greater-than-500Hz impedance-control result, real-time-kernel requirement, serial-buffer tuning or safe physical operating configuration is established here. The previous generic tuning instructions are not retained as a device procedure. See [ROS source status](../ros2-integration/overview.md) for what the publisher actually implements.
