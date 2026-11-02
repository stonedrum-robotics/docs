# MuJoCo integration questions

`Hand.mock()` is not a physics simulator. The demo-apps MuJoCo entry point prints a request for MJCF assets and controller bindings; it does not load a scene or simulate contact.

## Separate the proposed layers

A future simulation experiment needs a model with geometry, inertial/actuator parameters and joint conventions, an implementation mapping SDK targets/state to that simulator, and a defined validation task. The source/version and reuse terms of any model must also be established.

A shared Python method signature does not establish contact fidelity, sim-to-real transfer or a working `MujocoHand` adapter. No such adapter or qualified model is supplied by the current mock example.

Begin with [stored joint values](01-basic-control.md) to understand the interface. A simulation result would need its own pinned scene, controller, software environment and measurements; this documentation repair did not run MuJoCo.
