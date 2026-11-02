# ROS interface source status

## Actual publication path

`HandNode` creates a `sensor_msgs/msg/JointState` publisher using the relative name `joint_states`. A relative topic may resolve differently under a ROS namespace; this source does not establish the historical `/hand/joint_states` absolute name.

The callback copies the mock's joint names and stored positions into the message. Velocity/effort use the mock state's default values; they are not readings from hardware. A source timer period is not a measured rate or latency guarantee.

## Interfaces not implemented here

The inspected node classes do not create the former documented joint-command/glove subscriptions, a grasp action server or command services. The names `/hand/joint_commands`, `/teleop/glove_state` and `/execute_grasp` are therefore not supplied as working endpoints by these classes.

A future interface proposal should specify message types, naming/namespaces, timestamps, units and error behavior, then verify the running graph in a pinned environment. This repair did not execute ROS nodes.
