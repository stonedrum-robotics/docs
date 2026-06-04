# Troubleshooting Guide

This guide provides diagnosis and fix strategies for the most common errors encountered when working with the Dexterous Hand SDK.

## Python SDK Errors

### `ModuleNotFoundError`
- **Diagnosis**: Python cannot locate the `dexterous_hand` package.
- **Fix**: Ensure that your virtual environment is activated and that the package is installed properly (`pip install -e .` from the repository root).

### `RuntimeError: Hand not connected`
- **Diagnosis**: The SDK attempted physical communication but failed to establish a connection with the hand over USB/Serial.
- **Fix**: Check that the physical cable is securely connected. Verify that the correct USB port permissions are set (e.g., `sudo usermod -a -G dialout $USER` on Linux) and that the device shows up in `/dev/ttyUSB*` or `/dev/ttyACM*`.

### `KeyError: unknown joint name`
- **Diagnosis**: You provided a joint name to a method (like `move_joints`) that does not match the standardized naming convention.
- **Fix**: Ensure you are only using valid names: `thumb_flex`, `index_flex`, `middle_flex`, `ring_flex`, `little_flex`.

### `ValueError: joint position out of bounds`
- **Diagnosis**: The position command violated the soft limits enforced by `validate_positions()`.
- **Fix**: Adjust your target joint angles to ensure they fall within the safe operating range defined in the `lower_limits_rad` and `upper_limits_rad` properties.

## ROS 2 Errors

### ROS2 package not found
- **Diagnosis**: The ROS 2 workspace is not sourced, or the package was not built.
- **Fix**: Run `colcon build` in your workspace root, and ensure you run `source install/setup.bash` before launching nodes.

### ROS2 node publishes no joint states
- **Diagnosis**: The ROS 2 driver node is running, but the `/joint_states` topic is empty.
- **Fix**: Verify hardware connectivity. If using simulation, ensure `use_sim_time` is correctly configured and the simulator is actively ticking.

## Docker Errors

### Docker USB device not passed through
- **Diagnosis**: The containerized application fails to detect the hardware, resulting in connection timeouts.
- **Fix**: You must explicitly pass the device to the container. Use the `--device` flag when running the container (e.g., `docker run --device=/dev/ttyUSB0 ...`) or add the corresponding `devices:` mapping in your `docker-compose.yml`.
