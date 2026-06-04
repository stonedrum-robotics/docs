# Universal Robots Integration
This page summarizes the integration guide for mounting a Linkerbot L20 Lite, L20, or L30 hand on Universal Robots e-Series arms (UR5e / UR10e). 

For the complete, detailed instructions, please refer to the [Full UR Series Integration Guide](https://github.com/stonedrum-robotics/hardware-resources/blob/main/integration-guides/ur-series.md).

## 5-Step Integration Checklist
1. **Mechanical Mounting**: Fabricate and attach a rigid adapter plate (UR-side ISO 9409-1-50-4-M6 to Linkerbot-side `[VENDOR_SPEC_REQUIRED]`). Torque all M6 fasteners appropriately.
2. **Electrical Setup**: Provide a dedicated, fused external DC power supply (`[VENDOR_SPEC_REQUIRED]`). Do NOT power the hand directly from the UR tool connector.
3. **Communication Setup**: Wire the CAN/CAN FD or RS-485 lines to your host PC using shielded twisted-pair cables. Ensure proper termination (`[VENDOR_SPEC_REQUIRED]`).
4. **Robot Configuration**: Update the payload, TCP, and center of gravity in PolyScope to account for the hand, adapter, and cables.
5. **Software & Testing**: Install the ROS 2 packages, update the URDF with a fixed joint at `tool0`, and verify communication in mock mode before enabling real hardware motion.

## ROS 2 Launch Snippet
Add the following to your ROS 2 launch file to start the hand node alongside the UR driver:

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
