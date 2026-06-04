# Hand Model

The Stonedrum Robotics L20 dexterous hand features a highly capable multi-fingered design tailored for advanced manipulation tasks. Understanding its underlying kinematic and dynamic model is crucial for effective research and development.

## Degrees of Freedom (DOF)

The L20 features a sophisticated 21 DOF model. This is broken down into:
- **16 Active DOF**: Joints that are directly driven by individual actuators.
- **5 Coupled DOF**: Joints that are mechanically linked to other active joints, reducing complexity while maintaining natural motion profiles.

This configuration balances the complexity of the control problem with the dexterity required for fine manipulation tasks.

## Joint Naming Convention

The Dexterous Hand SDK uses a standardized naming convention to address the main flexor joints of each finger. When commanding the hand or reading its state, the following joint names are used:
- `thumb_flex`
- `index_flex`
- `middle_flex`
- `ring_flex`
- `little_flex`

This convention ensures consistency across the SDK, ROS 2 nodes, and simulation environments.

## State Representation

The SDK represents the hand's state using robust Python dataclasses. 

### `JointState` Dataclass
The `JointState` dataclass encapsulates the instantaneous state of a single actuated joint. It includes:
- `name` (str): The standardized name of the joint.
- `position_rad` (float): The current position of the joint in radians.
- `velocity_rad_s` (float): The joint velocity in radians per second (defaults to 0.0).
- `effort_nm` (float): The joint effort or torque in Newton-meters (defaults to 0.0).

### `Finger` Dataclass
The `Finger` dataclass models a named finger, its ordered joints, and the configured safety limits:
- `name` (str): The name of the finger.
- `joint_names` (list[str]): An ordered list of joint names associated with the finger.
- `lower_limits_rad` (list[float]): The minimum allowable joint angles in radians.
- `upper_limits_rad` (list[float]): The maximum allowable joint angles in radians.

## Joint Limit Validation

Safety is paramount when working with hardware. The `Finger` class implements strict position validation via the `validate_positions(positions_rad)` method. 

When a position command is issued:
1. The SDK verifies that the number of provided positions matches the number of expected joints.
2. It iteratively checks each position against its respective `lower_limits_rad` and `upper_limits_rad`.

If any limit is exceeded, the SDK immediately raises a `ValueError` with a descriptive message (e.g., `thumb_flex position 1.200 rad outside [0.000, 1.000]`), preventing the hardware from attempting an unsafe or physically impossible configuration.
