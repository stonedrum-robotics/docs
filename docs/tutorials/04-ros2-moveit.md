# MoveIt 2 integration questions

The current public source does not provide a validated combined arm-hand MoveIt configuration. The demo-apps MoveIt entry point prints setup expectations; it does not launch a supplied planning configuration.

## What a future planning experiment needs

A planning setup needs a precise robot description, joint conventions/limits, geometry, semantic groups, controllers and a mapping between planning output and an implemented backend. Model provenance and permitted use must be established for the selected files. Collision checking in a model is distinct from qualification of physical operation.

The SDK's mock does not supply a device URDF, collision model or controller bridge. Its five software joint names cannot be used as evidence of a named hand's full kinematics.

Use the [ROS source status](../ros2-integration/overview.md) to inspect existing scaffolding. This page intentionally offers no run-ready arm/hand launch command or SRDF recipe; those require actual configuration and environment validation.
