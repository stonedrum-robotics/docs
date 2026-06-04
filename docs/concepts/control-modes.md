# Control Modes

The Dexterous Hand SDK provides robust control interfaces for operating the hand in both physical and simulated environments.

## Current Mode: Position Control

Presently, the primary control mode exposed by the SDK is **Position Control**. In this mode, users specify target joint angles in radians. 

When a position command is issued:
1. The desired joint positions are validated against hardware limits.
2. The targets are transmitted to the hand's low-level controllers.
3. The internal PID controllers drive the actuators to reach the target angles.

This mode is ideal for pick-and-place tasks, predefined grasp execution, and kinematic planning.

## Future Modes `[PLANNED]`

To support advanced manipulation and physical interaction research, future releases will introduce the following modes:
- **Velocity Control `[PLANNED]`**: Direct commanding of joint velocities (rad/s) for smoother continuous motion profiles.
- **Torque / Effort Control `[PLANNED]`**: Direct commanding of joint torques (Nm) to enable dynamic tasks and underactuated grasping.
- **Impedance Control `[PLANNED]`**: Allows tuning of virtual stiffness and damping parameters, enabling compliant interaction with fragile objects and unstructured environments.

## Coordinate Frames

Understanding the operational spaces is critical for control:
- **Joint Space**: The native configuration space of the hand. Commands are arrays of joint angles (e.g., `thumb_flex = 0.5 rad`). The SDK currently operates purely in Joint Space.
- **Task Space `[PLANNED]`**: The Cartesian space (X, Y, Z, Roll, Pitch, Yaw) representing the position and orientation of the fingertips or the manipulated object. Future inverse kinematics (IK) solvers will translate Task Space objectives into Joint Space commands.

## Safety Mechanisms

The SDK incorporates multi-layered safety mechanisms tightly integrated into the control pipeline.

- **Soft Limits**: Every position command is intercepted by `validate_positions()`. This enforces strict lower and upper angular bounds before any command reaches the hardware, preventing self-collision and hyper-extension.
- **Emergency Stop**: For immediate halting of all motion, the `hand.stop()` method is available. This bypasses normal trajectory execution and immediately arrests actuator movement.
