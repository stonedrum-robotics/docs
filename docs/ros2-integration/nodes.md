# ROS 2 node source status

The following descriptions refer to the SDK commit named on the [home page](../index.md); they are static source observations, not a successful ROS runtime demonstration.

| Source class | Implemented behavior |
|---|---|
| `HandNode` | Constructs `Hand.mock()`, creates a publisher on relative topic `joint_states` with depth10, and a0.02-second timer calling `publish_joint_states()` |
| `TeleoperationNode` | Initializes a node and logs a startup message; no input subscription or mapping loop |
| `GraspActionServer` | Initializes a node and logs a placeholder message; no action server implementation |

`HandNode` populates names, positions, velocities and efforts from mock `JointState` values. That does not make them measured device telemetry or establish achieved publishing frequency.

These files guard optional ROS imports; their `main()` functions require `rclpy`. Configuration keys in a YAML file are not proof that a node reads/applies them. There is no demonstrated hardware-backend selector, live glove controller or physical grasp action in these classes. See [topics and services](topics-services.md).
