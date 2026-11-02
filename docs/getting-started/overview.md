# Overview

A hand interface gives application code names for joint targets and states. In this SDK, `Hand` delegates operations to a backend implementing `HandDriver`; `Hand.mock()` connects a five-joint in-memory backend.

## What the current source provides

- Stored joint positions and `JointState` objects.
- Nine primary grasp target sets and three compatibility entries.
- A frame object and controller for applying supplied joint targets.
- Unsupported vendor adapter classes that raise `NotImplementedError` for hardware operations.

The default joint list is a software example, not a model of a named manufacturer's complete hand. A shared Python interface does not make mock and hardware behavior equivalent or establish interchangeability.

## Choosing a starting point

Use [first movement](first-movement.md) for a small offline example. Read [hand model](../concepts/hand-model.md) for field definitions and [safety scope](../concepts/safety.md) for the limits of software checks. The ROS 2 and simulation sections describe their own incomplete integration status; no supported multi-platform or physical-device matrix is claimed here.
