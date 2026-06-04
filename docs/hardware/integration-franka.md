# Franka Panda / FR3 Integration
This page summarizes the integration guide for mounting a Linkerbot L20 Lite, L20, or L30 hand on Franka Research 3 (FR3) and Franka Emika Panda arms.

For the complete, detailed instructions, please refer to the [Full Franka Integration Guide](https://github.com/stonedrum-robotics/hardware-resources/blob/main/integration-guides/franka-panda.md).

## 5-Step Integration Checklist
1. **Mechanical Mounting**: Use an adapter plate (Franka-side ISO 9409-1-50-4-M6 to Linkerbot-side `[VENDOR_SPEC_REQUIRED]`). Ensure the hand is mounted as close to the wrist as possible to preserve Cartesian compliance behavior.
2. **Electrical Setup**: Provide a dedicated, fused external DC power supply (`[VENDOR_SPEC_REQUIRED]`). Do NOT use the Franka controller to power the hand.
3. **Communication Setup**: Wire the CAN/CAN FD or RS-485 lines to your host PC. Route cables with enough slack to avoid biasing force-torque behavior during impedance control experiments.
4. **Robot Configuration**: Set the exact end-effector mass, inertial estimate, and center of gravity in the Franka control stack before enabling motion.
5. **Software & Testing**: Install the ROS 2 packages, attach the hand to the `fr3_hand_tcp` (or appropriate Panda TCP link) in the URDF, and run mock-mode tests before engaging hardware.

## ROS 2 Launch Snippet
Add the following to your ROS 2 launch file to start the hand node alongside the `franka_ros2` control stack:

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description() -> LaunchDescription:
    return LaunchDescription(
        [
            Node(
                package="dexterous_hand_ros2",
                executable="hand_node",
                name="dexterous_hand",
                output="screen",
            )
        ]
    )
```
