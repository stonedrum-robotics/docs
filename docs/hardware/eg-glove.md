# EG Glove
The EG Glove is a wireless motion-capture exoskeleton glove designed for seamless teleoperation of Linkerbot dexterous hands. Built by Stonedrum Robotics, the glove provides high-fidelity tracking of human hand movements with a capture precision of 0.005°. Weighing just 190g and utilizing ESP-NOW wireless transmission (50Hz, 20m indoor range), it offers an untethered and ergonomic solution for collecting human demonstration data or controlling robotic hands in real-time.

## Software Integration
The EG Glove connects to the Linkerbot SDK via the `TeleoperationController` class, which handles the mapping of glove telemetry to robotic hand commands.

### Calibration Steps
1. Power on the EG Glove and ensure the wireless receiver is connected to the host PC.
2. Hold your hand in a flat, relaxed pose.
3. Trigger the zero-calibration routine via the SDK (`[VENDOR_SPEC_REQUIRED]` for exact API call).
4. Perform a full fist closure to calibrate the maximum joint limits.

### Teleoperation Flow
The standard software loop for controlling a hand with the EG Glove is as follows:

1. **`read_glove_frame()`**: This method polls the glove hardware for the latest joint angles and returns a normalized `TeleoperationFrame`.
2. **`apply_frame()`**: The controller receives the frame and processes it.
3. **`hand.move_joints()`**: The joint targets from the frame are sent to the robotic hand hardware for execution.

### Note on `read_glove_frame()`
Currently, the `read_glove_frame()` method in the base SDK raises a `NotImplementedError("Glove device integration is vendor-specific.")`. Because different labs use different receivers and serial protocols for the ESP-NOW bridge, the exact hardware reading logic must be implemented by the user or provided via a vendor-specific plugin. You must subclass `TeleoperationController` and implement `read_glove_frame()` to interface with your specific receiver hardware.
