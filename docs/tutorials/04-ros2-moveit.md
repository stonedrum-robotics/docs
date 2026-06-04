# Tutorial 4: ROS 2 and MoveIt 2 Setup

Integrating the Stonedrum Robotics dexterous hand with MoveIt 2 allows you to perform complex motion planning, collision avoidance, and trajectory execution. While `examples/04_ros2_demo.py` shows basic launch commands, this tutorial explains the broader MoveIt 2 setup.

## MoveIt 2 Setup

MoveIt 2 relies heavily on the Semantic Robot Description Format (SRDF) and the Universal Robot Description Format (URDF). To use MoveIt 2, you must configure a move group that defines the kinematic chain of the hand.

**Steps to Configure:**
1. Generate a URDF for your robot arm and attach the Stonedrum hand to the end-effector link.
2. Use the MoveIt Setup Assistant to generate the MoveIt 2 configuration package.
3. Define a planning group (e.g., `hand`) encompassing the finger joints.
4. Define End Effector (EEF) poses in the SRDF that mirror the Grasp Library (e.g., "open", "pinch").

## Launch Steps

Once your MoveIt 2 configuration package is built, you can launch the stack. First, ensure the `HandNode` is running so joint states are available.

From your ROS 2 workspace:
```bash
# Terminal 1: Launch the hand node
ros2 launch dexterous_hand_ros2 hand.launch.py mock:=true

# Terminal 2: Launch MoveIt 2 (assuming a custom config package)
ros2 launch my_robot_moveit_config demo.launch.py
```
This will open RViz, allowing you to use the interactive markers to plan trajectories for the fingers and arm simultaneously.

## SRDF Snippet

Here is an example snippet of how you might define the "open" pose in your SRDF file for the hand planning group:

```xml
<robot name="stonedrum_arm_hand">
    <group name="hand">
        <joint name="thumb_flex" />
        <joint name="index_flex" />
        <joint name="middle_flex" />
        <joint name="ring_flex" />
    </group>
    
    <!-- Define standard named states -->
    <group_state name="open" group="hand">
        <joint name="thumb_flex" value="0.0" />
        <joint name="index_flex" value="0.0" />
        <joint name="middle_flex" value="0.0" />
        <joint name="ring_flex" value="0.0" />
    </group_state>
</robot>
```

For more advanced MoveIt 2 configurations or custom IK solvers, contact info@stonedrum.co.
