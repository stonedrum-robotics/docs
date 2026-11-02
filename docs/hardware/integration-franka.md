# Franka Panda / FR3 integration planning

This route records integration questions rather than a validated Franka Panda / FR3/hand setup. The published SDK supplies no working vendor hand driver and no evidence of a commissioned combined arm-hand system.

## Separate the interfaces

An arm controller, mounting adapter, hand controller and application each have configuration-specific constraints. Record their exact models/revisions, manufacturer instructions, coordinate frames, load information, communications and stopping/responsibility boundaries before proposing physical work.

The existence of a flange standard or a generic ROS launch structure does not establish fit, electrical compatibility, collision geometry or a supported combined planning group. A qualified configuration-specific review is needed for those questions.

## Current available material

The [hardware-resources repository](https://github.com/stonedrum-robotics/hardware-resources) contains preliminary planning notes, not qualified designs. The [ROS source overview](../ros2-integration/overview.md) distinguishes actual mock publication code from placeholders. No arm launch/commissioning recipe is offered by this page.
