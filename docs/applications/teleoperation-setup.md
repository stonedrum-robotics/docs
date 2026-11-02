# Teleoperation integration planning

The public source does not establish a working glove-to-hand rig. `read_glove_frame()` is unimplemented, and the ROS teleoperation node currently logs a startup message without implementing a live subscription/mapping loop.

## Plan the boundaries before connecting devices

Specify the input device/interface, coordinate and unit conventions, timestamp behavior, mapping/calibration method, output backend and response to missing or invalid data. A physical setup also needs exact manufacturer documentation and configuration-specific engineering/safety review.

Treat captured human or facility information according to a separately defined collection and permitted-use scope. None of those responsibilities is solved by the `TeleoperationFrame.source` label.

The [canned Python tutorial](../tutorials/03-teleoperation.md) demonstrates only applying supplied numbers to a mock. It is a useful starting interface example, not evidence of a calibrated 1:1 rig, live recording pipeline or supported installation service.
