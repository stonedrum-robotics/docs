# Safety Guidelines

When operating the Stonedrum Robotics L20 dexterous hand, adhering to strict safety protocols is mandatory to protect both the operator and the hardware.

## Operating Limits

The hardware is designed to operate within specific physical parameters. Exceeding these can result in degraded performance or permanent damage.
- **Joint Velocity**: Avoid commanding instantaneous large step changes in joint positions. Use smooth trajectories where possible.
- **Payload**: The hand is rated for a specific maximum payload. Do not attempt to grasp objects exceeding the specified mass limit.
- **Temperature**: Continuous high-torque operation can elevate actuator temperatures. The system should be allowed to cool if the external casing becomes hot to the touch.

## Emergency Stop

In the event of unexpected behavior, imminent collision, or hardware faults, immediate cessation of movement is required.
- **`hand.stop()`**: The SDK provides an emergency stop method. Calling `hand.stop()` immediately halts all active joint motions by commanding zero velocity to the actuators.
- **When to call it**: Use this programmatic stop in error-handling routines, physical kill-switch callbacks, or anytime anomalous behavior is detected during execution.

## Mock Mode Evaluation

The safest path for initial development and evaluation is the Mock Mode.
- By instantiating the hand via `Hand.mock()`, you create a purely software-based representation of the hand.
- Use Mock Mode to test complex logic, validate grasp sequences, and ensure your code behaves correctly before running it on physical hardware.

## CE Certification Status

Please note that the CE certification for the Stonedrum Robotics L20 hand is **under verification**. For inquiries regarding compliance or certification updates, please contact info@stonedrum.co.

## Physical & Software Safety

Safety relies on a combination of physical awareness and robust software design.
- **Physical Safety**: Keep hands, loose clothing, and cables away from the robotic hand while it is powered. Operate the hand in a designated workspace free from unexpected obstructions.
- **Software Safety**: Always ensure your application catches exceptions gracefully and issues a `hand.stop()` on failure. Rely on the SDK's built-in `validate_positions()` to enforce soft limits, but do not bypass hardware-level safeguards.
