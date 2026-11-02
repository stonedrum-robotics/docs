# Linkerbot L30

These names refer to external Linkerbot products, not hardware designed or manufactured by Stonedrum Robotics. The current public SDK does not establish support for a selected product variant.

## Product evaluation questions

For a specific unit, obtain a versioned manufacturer specification and record the controller, firmware and mechanical revision. Compare requirements for kinematics, actuation, sensing, electrical interface, protocol and mounting against that exact configuration. A similar product name is not enough to transfer a specification between variants.

The former numeric tables, pinout diagrams and generic operating instructions are not retained as verified product facts. This page does not supply qualified dimensions, payload, precision, speed, wiring, supply values, conformity status or interoperability claims.

## Software boundary

`LinkerbotDriver` is an unsupported adapter placeholder. Hardware operations raise `NotImplementedError` before transport I/O. A named pose in `GraspLibrary` is a mock target set, not a calibrated command for this hand. See [hardware setup status](../getting-started/hardware-setup.md) and [safety scope](../concepts/safety.md).
