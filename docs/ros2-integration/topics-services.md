# Topics, Services, and Actions

| Interface | Type | Name | Message/Service Type | Description |
|-----------|------|------|----------------------|-------------|
| Topic | Pub | `/hand/joint_states` | `sensor_msgs/msg/JointState` | Current hand state |
| Topic | Sub | `/hand/joint_commands` | `sensor_msgs/msg/JointState` | Desired joint targets |
| Action | Server| `/hand/execute_grasp` | custom Action | Executes a named grasp |
| Service | Server| `/hand/set_control_mode`| custom Srv | Switches between Position/Torque |
