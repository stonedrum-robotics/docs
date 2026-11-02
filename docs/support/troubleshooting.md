# Troubleshooting the mock source

## Import errors

If `dexterous_hand` cannot be imported, check that you are using the intended Python interpreter and the pinned SDK source directory, then use `PYTHONPATH=.` as in [source setup](../getting-started/installation.md). This does not diagnose an unavailable registry package or ROS/container installation.

## Connection state

`Hand.mock()` connects its backend automatically. A manually constructed `MockHandDriver` needs `connect()` before its checked operations; otherwise it raises `RuntimeError("Driver is not connected")`.

## Names and ranges

An unknown target key raises `KeyError` in the mock. Compare with the default software joint names. `Finger.validate_positions()` separately raises `ValueError` for a wrong list length or a value outside its configured bounds. `Hand.move_joints()` does not automatically invoke that range validator.

## Unsupported operations

Vendor hardware operations and glove reading deliberately raise `NotImplementedError`. Do not treat those errors as a cabling problem or bypass them to send unverified commands. ROS node logging/publisher source is not a working grasp action or live teleoperation path.

For a report, include the exact commit and a minimal redacted mock reproduction through [contact and reports](contact.md).
