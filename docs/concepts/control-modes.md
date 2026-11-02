# Command and control behavior

## Current in-memory behavior

`Hand.move_joints()` forwards a dictionary of position targets to its backend. `MockHandDriver` rejects unknown joint names and updates its stored values immediately. It has no physical trajectory, velocity controller, force feedback or timing model.

`Hand.move_to_grasp(name)` looks up a target dictionary and forwards it. `Hand.open()` requests zero targets for the backend's reported joints. The `open` grasp entry is different: its empty target dictionary leaves existing mock values unchanged.

## Validation and stopping

The separate `Finger.validate_positions()` method checks caller-provided values against configured ranges. The general hand command path does not promise to perform that check. Software ranges are not evidence of collision-free or safe physical motion.

`Hand.stop()` requests backend-specific behavior. In the mock it has no physical action; unsupported vendor adapters raise `NotImplementedError`. It is not an implemented physical emergency stop. See [safety scope](safety.md).

No physical position, velocity, effort or impedance-control mode is established by the mock example. A future backend needs explicit implementation and its own validation.
