# Imitation-learning preparation

A proposed imitation-learning experiment needs a defined observation/action representation, timing and task context. Data collection, training and policy evaluation are different pieces of work, each needing explicit source and version records.

## Current interface examples

`TeleoperationFrame` can hold supplied joint targets. It does not record human demonstrations, synchronize cameras/sensors, manage dataset permissions or load/train a policy. The RL demo entry point prints an integration instruction; no trained model or inference implementation is supplied there.

Before using a collected dataset, establish provenance, permitted uses and the applicable privacy/workflow requirements. Before making transfer claims, evaluate the exact policy, embodiment mapping and target task. No ACT/Diffusion Policy compatibility, distribution service or automatic retargeting result is established by the current SDK.

Use [canned frames](../tutorials/03-teleoperation.md) for an offline interface exercise and [training-data concepts](../concepts/training-data.md) for candidate metadata questions.
