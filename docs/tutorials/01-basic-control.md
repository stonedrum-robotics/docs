# Tutorial 1: stored joint values

Use the pinned source setup and run this in the SDK directory with `PYTHONPATH=.`:

```python
from dexterous_hand import Hand

hand = Hand.mock()
hand.move_joints({"thumb_flex": 0.2, "index_flex": 0.4})
print({s.name: s.position_rad for s in hand.read_joints()})
hand.open()
print([s.position_rad for s in hand.read_joints()])
```

The first print contains the two supplied values and zero for the remaining joints. The second print is a list of five zeros. There is no physical motion or trajectory; `MockHandDriver` updates an in-memory dictionary.

## Exercises

1. Change one known target and compare the returned positions.
2. Try an unknown joint name and inspect the resulting `KeyError`.
3. Construct a `Finger` with explicit ranges and call `validate_positions()` separately; compare its errors with the mock command interface.

Do not infer automatic range checking or collision protection from this example. `Hand.move_joints()` does not call `Finger.validate_positions()`. Hardware adapters remain unsupported; see [control behavior](../concepts/control-modes.md).
