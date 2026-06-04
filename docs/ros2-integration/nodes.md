# ROS 2 Nodes

The Stonedrum Robotics ROS 2 ecosystem provides three primary nodes to interact with the dexterous hand. Each node manages a specific domain: hardware bridging, human-in-the-loop teleoperation, and high-level grasping logic.

## HandNode

**Purpose:** 
The `HandNode` serves as the fundamental bridge between the ROS 2 network and the Stonedrum Robotics Python SDK. It instantiates the hardware or mock driver, reads joint states at a fixed loop rate (default 50Hz), and publishes telemetry to `/hand/joint_states`. It also subscribes to joint commands, converting incoming messages into hardware actuation.

**Parameters:**

| Parameter Name | Type   | Default | Description |
|----------------|--------|---------|-------------|
| `mock_mode`    | bool   | `true`  | If true, initializes `Hand.mock()`. If false, attempts to connect to real hardware. |
| `publish_rate` | double | `50.0`  | The frequency (in Hz) at which joint states are queried and published. |
| `hand_id`      | string | `hand1` | Identifier for the hand, used to namespace topics and frame IDs. |

**How to Launch:**
```bash
ros2 run dexterous_hand_ros2 hand_node --ros-args -p mock_mode:=false
```

**Example:**
In a typical use case, you would start the `HandNode` to get the hand's current position to show up in RViz. 

## TeleoperationNode

**Purpose:**
The `TeleoperationNode` translates external user input—like a keyboard or a VR glove—into normalized `TeleoperationFrame` messages. It uses the `TeleoperationController` from the Python SDK to map these generic frames into specific joint targets for the `HandNode`. This node abstracts away vendor-specific integrations.

**Parameters:**

| Parameter Name | Type   | Default    | Description |
|----------------|--------|------------|-------------|
| `input_device` | string | `keyboard` | The type of input device (`keyboard`, `glove`, etc.). |
| `scaling`      | double | `1.0`      | A multiplier for the raw input signals before they are converted to joint limits. |

**How to Launch:**
```bash
ros2 run dexterous_hand_ros2 teleoperation_node --ros-args -p input_device:=keyboard
```

**Example:**
Running this node allows a user to press keys on their keyboard to actuate the hand in real-time, streaming the results directly to the `/teleop/glove_state` topic.

## GraspActionServer

**Purpose:**
The `GraspActionServer` provides a high-level ROS 2 Action interface for executing named grasps (e.g., "pinch", "cylindrical"). It receives an action goal containing a target grasp string, expands it using the SDK's `GraspLibrary`, and publishes a smooth trajectory of joint commands to the `HandNode`. It provides feedback on the grasp's progress and returns a final success state.

**Parameters:**

| Parameter Name | Type   | Default | Description |
|----------------|--------|---------|-------------|
| `duration`     | double | `2.0`   | The time (in seconds) the server should take to interpolate from the current pose to the target grasp. |

**How to Launch:**
```bash
ros2 run dexterous_hand_ros2 grasp_action_server
```

**Example:**
A MoveIt 2 pipeline can call this action server to close the hand around an object after the robotic arm has navigated to the pre-grasp pose. The action client waits until the hand confirms it has successfully reached the "pinch" configuration before moving the arm away. For support, reach out to info@stonedrum.co.
