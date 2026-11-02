# First mock joint update

After [source setup](installation.md), run from the pinned SDK directory:

```bash
PYTHONPATH=. python3 - <<'PYTHON'
from dexterous_hand import Hand

hand = Hand.mock()
hand.move_joints({"thumb_flex": 0.25, "index_flex": 0.4})
for state in hand.read_joints():
    print(f"{state.name}: {state.position_rad:.2f} rad")
hand.open()
hand.stop()
PYTHON
```

Expected joint-state output:

```text
thumb_flex: 0.25 rad
index_flex: 0.40 rad
middle_flex: 0.00 rad
ring_flex: 0.00 rad
little_flex: 0.00 rad
```

`Hand.mock()` starts with five stored zero positions. `move_joints()` updates the named entries, and `read_joints()` returns their software state. `open()` requests zero targets for the reported joints. `stop()` checks the mock connection and performs no physical action.

This example neither moves a device nor simulates one. Swapping a constructor does not provide a working hardware integration: current vendor adapters reject unsupported operations. See [hardware setup status](hardware-setup.md).
