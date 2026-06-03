# Basic Joint Control

This tutorial covers `examples/01_basic_joint_control.py`.

```python
from dexterous_hand import Hand

def main() -> None:
    hand = Hand.mock()
    hand.move_joints({"thumb_flex": 0.3, "index_flex": 0.4})
    for state in hand.read_joints():
        print(f"{state.name}: {state.position_rad:.2f} rad")

if __name__ == "__main__":
    main()
```

### Walkthrough
1. **Initialization**: We instantiate a mock hand which creates an in-memory mock driver.
2. **Commanding**: `move_joints` takes a dictionary of joint names and target radians.
3. **Feedback**: `read_joints` returns `JointState` objects which we print out.

**Expected Output:**
```
thumb_flex: 0.30 rad
index_flex: 0.40 rad
...
```
