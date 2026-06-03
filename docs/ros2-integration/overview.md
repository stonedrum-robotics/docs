# ROS 2 Integration Overview

The Stonedrum Robotics ROS 2 packages expose the Python SDK over standard ROS interfaces.

```mermaid
graph TD
    HandNode[HandNode] -->|sensor_msgs/JointState| JS[/hand/joint_states/]
    CMD[/hand/joint_commands/] --> HandNode
    TeleopNode[TeleoperationNode] -->|glove_state| TeleopTopic[/teleop/glove_state/]
    GraspActionServer[GraspActionServer] <-- execute_grasp action --> Client
```

These nodes abstract hardware complexities and enable standard ROS tools like RViz and MoveIt 2.
