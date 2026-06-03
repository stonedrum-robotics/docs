# Grasp Sequence

This tutorial covers `examples/02_grasp_sequence.py`.

```python
from dexterous_hand import Hand
import time

def main() -> None:
    hand = Hand.mock()
    for grasp in ["open", "pinch", "cylindrical", "open"]:
        hand.move_to_grasp(grasp)
        print(f"Applied grasp: {grasp}")
        time.sleep(1.0)

if __name__ == "__main__":
    main()
```

### Walkthrough
1. **Sequence**: We define a list of named grasps from the `GraspLibrary`.
2. **Execution**: `move_to_grasp` automatically translates the name into joint targets.
3. **Safety**: Starting and ending with "open" ensures safe transitions.

**Expected Output:**
```
Applied grasp: open
Applied grasp: pinch
Applied grasp: cylindrical
Applied grasp: open
```
