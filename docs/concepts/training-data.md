# Training-data concepts

A manipulation dataset can describe observations, actions, timestamps and the context in which they were collected. For a proposed dataset, useful fields include sensor/calibration metadata, joint naming and units, task boundaries, outcomes and provenance or permitted-use records.

## What the current SDK establishes

The public SDK contains hand/joint interfaces and supplied teleoperation frames. It does not include a `dexterous_hand.data` module, a synchronized recording pipeline, a dataset loader or a demonstrated policy-training/transfer system. A common command dictionary does not eliminate retargeting between different hardware or embodiments.

The in-memory mock does not provide measured tactile feedback, RGB-D synchronization or physical state-action trajectories. Mock values should be labeled as generated software examples rather than captured device data.

## Future data work

Any proposed collection, processing or distribution needs its own scope, source/provenance, permissions, privacy and technical validation. This page makes no GDPR compliance guarantee, dataset availability or partner-distribution claim, release date or early-access offer. Questions about a possible project can go to [info@stonedrum.co](mailto:info@stonedrum.co), without implying an existing data service.
