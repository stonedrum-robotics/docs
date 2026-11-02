# Tutorial 2: named target sequences

The SDK's `examples/02_grasp_sequence.py` creates `Hand.mock()` and calls `move_to_grasp()` for `open`, `pinch`, `cylindrical`, `open`, printing each name. Those are dictionary lookups and stored position updates; they do not establish a physical grasp.

## Inspect the state behind the labels

```python
from dexterous_hand import Hand

hand = Hand.mock()
for name in ["open", "pinch", "cylindrical", "open"]:
    hand.move_to_grasp(name)
    print(name, {s.name: s.position_rad for s in hand.read_joints()})
```

The first `open` leaves the initially zero values unchanged. The last `open` also leaves values unchanged, so the cylindrical targets remain stored. Historical example comments saying the sequence ends open are inaccurate. `Hand.open()` is a different method that requests zero joint targets.

## Exercises

- Compare `open`, `relaxed_open` and `Hand.open()` using printed software values.
- Retrieve `hand.grasps.get("tripod").joint_positions_rad` and inspect the values.
- Create a `GraspPose` for a mock exercise and pass its dictionary to `move_joints()`.

The [grasp vocabulary](../concepts/grasp-taxonomy.md) gives all nine primary sets and three compatibility entries. Target names and angles are not calibrated object-handling or safe-rest poses for a physical hand.
