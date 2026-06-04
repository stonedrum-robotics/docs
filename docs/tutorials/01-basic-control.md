# Tutorial 1: Basic Joint Control

In this tutorial, we will explore the simplest way to interact with the Stonedrum Robotics dexterous hand using the Python SDK. We will walk through `examples/01_basic_joint_control.py` to understand how to instantiate the driver, send commands, and read telemetry.

## Annotated Walkthrough

Let's look at the example script, `examples/01_basic_joint_control.py`:

```python
"""Basic joint control example."""

# Import the high-level API; it hides the concrete driver implementation.
from dexterous_hand import Hand

def main() -> None:
    """Command a mock hand and print joint states."""
    # Mock mode connects an in-memory driver, so this example is safe in CI.
    hand = Hand.mock()
    
    # Command two joints in radians; unspecified joints keep their last value.
    hand.move_joints({"thumb_flex": 0.3, "index_flex": 0.4})
    
    # Read back every joint state to confirm the command reached the driver.
    for state in hand.read_joints():
        # Print compact telemetry that mirrors what a ROS JointState would carry.
        print(f"{state.name}: {state.position_rad:.2f} rad")

if __name__ == "__main__":
    main()
```

### Mock Driver Internals

The key to this example is the `Hand.mock()` initialization. When you call this method, the SDK loads an in-memory "dummy" driver instead of attempting to communicate over a serial or network port to real hardware. 

The mock driver perfectly simulates the API surface. When `move_joints()` is called, it stores the target positions in memory. When `read_joints()` is subsequently called, it immediately returns those target positions as the current state, assuming instantaneous and perfect execution. This allows you to write tests, validate control logic, and run continuous integration pipelines without requiring a physical Linkerbot hardware connection on your desk.

To connect to real hardware later, you would simply replace `Hand.mock()` with `Hand(port='/dev/ttyUSB0')` (or the equivalent connection string for your setup).

## Exercises

1. **Modify Joint Targets**: Change the script to actuate the `middle_flex` and `ring_flex` joints to `0.5` radians. Run the script and verify the output.
2. **Read Specific Joints**: Instead of iterating over all joints, modify the `read_joints()` logic to only print the state of the `thumb_flex` joint.
3. **Simulate a Sequence**: Put the `move_joints` and `read_joints` calls inside a `for` loop, slowly incrementing the `index_flex` position from `0.0` to `1.0` radians in steps of `0.1`.

If you have questions about the basic control API, contact us at info@stonedrum.co.
