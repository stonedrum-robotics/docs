# Launch Files

Launch files simplify starting the hand nodes with the correct parameters.

```bash
ros2 launch dexterous_hand_ros2 hand.launch.py use_mock:=false port:=/dev/ttyUSB0
```

**Parameters:**
- `use_mock`: Set to `true` for simulation/testing without hardware.
- `port`: Serial port for the hardware driver.
- `baudrate`: Communication speed.
