# EG Glove integration questions

The EG Glove is referenced as external capture hardware. This documentation does not establish its manufacturer identity, precise product variant, sensor performance, wireless protocol or compatibility with a Stonedrum SDK integration.

## Current Python behavior

`TeleoperationFrame` holds supplied joint targets and a source label. `TeleoperationController.apply_frame()` forwards nonempty targets to a `Hand`. `read_glove_frame()` raises `NotImplementedError`; there is no live glove reader, automatic calibration or demonstrated 1:1 hand mapping in this path.

## Before a device integration

Identify the manufacturer and exact hardware/software revision, obtain its interface and calibration documentation, then define coordinate conventions, units, timestamp behavior and missing-data handling. Captured human or facility data also needs its own collection and permitted-use scope.

No generic calibration routine or device operating procedure is supplied here. The [canned frame tutorial](../tutorials/03-teleoperation.md) shows the software interface without connecting a glove.
