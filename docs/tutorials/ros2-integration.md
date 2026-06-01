# ROS 2 Integration

Launch the hand node:

```bash
ros2 launch dexterous_hand_ros2 hand.launch.py mock:=true
```

The node publishes `sensor_msgs/JointState` on `joint_states`.
