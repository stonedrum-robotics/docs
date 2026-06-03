# Troubleshooting

**Hand fails to connect:**
- Check power supply.
- Ensure `/dev/ttyUSB0` has the correct permissions (`sudo usermod -aG dialout $USER`).

**ROS 2 Node crashes on start:**
- Verify that `use_mock` is correctly set if hardware is not attached.
