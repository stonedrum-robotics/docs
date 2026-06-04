# Launch Files

The Stonedrum Robotics ROS 2 package provides standard Python-based launch files to initialize the system quickly. These launch files manage node lifecycle, load parameters, and can map topics as necessary.

## Available Launch Files

### `hand.launch.py`
The primary launch file for bringing up the dexterous hand. It starts the `HandNode` and optionally starts the `GraspActionServer` and `TeleoperationNode` based on arguments.

**Arguments:**
- `mock` (default: `true`): If `true`, the `HandNode` initializes the software mock driver (`Hand.mock()`). If `false`, it connects to physical hardware.
- `use_teleop` (default: `false`): If `true`, launches the `TeleoperationNode` with a default keyboard layout.
- `start_action_server` (default: `true`): If `true`, launches the `GraspActionServer` to handle high-level named grasps.

## Code Example

To launch the system in simulation/mock mode with the grasp action server running, use the following terminal command:

```bash
ros2 launch dexterous_hand_ros2 hand.launch.py mock:=true start_action_server:=true
```

To include this launch file inside a larger system launch (like an arm + hand setup), you can use the ROS 2 Python launch API:

```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    hand_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('dexterous_hand_ros2'),
                'launch',
                'hand.launch.py'
            ])
        ]),
        launch_arguments={
            'mock': 'false',
            'use_teleop': 'false'
        }.items()
    )

    return LaunchDescription([
        hand_launch
    ])
```
For advanced configurations, contact us at info@stonedrum.co.
