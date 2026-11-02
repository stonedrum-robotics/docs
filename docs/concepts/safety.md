# Safety scope

The current Python reference SDK and its mock tests do not qualify a physical hand, robot controller or installation for operation.

## What software operations mean

- `Hand.stop()` is a backend request. The mock performs no physical action; unsupported vendor operations raise `NotImplementedError`. It does not provide a physical emergency-stop function.
- `Finger.validate_positions()` checks a list against configured numeric ranges when called explicitly. It does not prove collision avoidance, safe contact or protection from physical harm.
- Mock positions are stored values, not sensed motion or a physical simulation.

## Before any physical work

A future hardware integration needs exact manufacturer instructions and a configuration-specific engineering and safety review, including the actual equipment stopping functions and responsibility boundaries. These documentation pages cannot supply missing controller, wiring, mounting, calibration or conformity evidence.

For an immediate equipment risk, follow the equipment manufacturer's emergency and safety procedures; email is not an emergency channel. Suspected software vulnerabilities or unsafe behavior can be reported privately to [info@stonedrum.co](mailto:info@stonedrum.co). No response or fix timeline is promised here.

Use [the offline example](../getting-started/first-movement.md) to inspect software behavior without connecting hardware.
