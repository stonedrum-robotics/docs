# Realtime Performance

For high-frequency control (e.g., >500Hz impedance control), a realtime kernel is required.

1. Install `linux-image-rt` on Ubuntu.
2. Configure GRUB to boot into the RT kernel.
3. Ensure the serial port latency timer is set to 1ms:
   ```bash
   setserial /dev/ttyUSB0 low_latency
   ```
