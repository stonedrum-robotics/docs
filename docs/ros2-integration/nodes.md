# ROS 2 Nodes

- **HandNode**: The core driver node. It instantiates the `Hand` class, publishes `/hand/joint_states`, and subscribes to `/hand/joint_commands`.
- **TeleoperationNode**: Interfaces with the EG Glove or other teleoperation devices, streaming joint targets.
- **GraspActionServer**: Provides an Action interface to execute pre-defined grasps from the Grasp Library with feedback.
