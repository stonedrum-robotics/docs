# Tutorial 3: supplied teleoperation frames

`examples/03_teleoperation_keyboard.py` is a canned mock example. It does not read keyboard events or a glove. The useful software boundary is a frame containing supplied target values:

```python
from dexterous_hand import Hand
from dexterous_hand.teleoperation import TeleoperationController, TeleoperationFrame

hand = Hand.mock()
controller = TeleoperationController(hand)
frame = TeleoperationFrame({"thumb_flex": 0.5, "index_flex": 0.5}, "exercise")
controller.apply_frame(frame)
print({s.name: s.position_rad for s in hand.read_joints()})
```

`apply_frame()` forwards nonempty target dictionaries. An empty dictionary returns without a command. `read_glove_frame()` raises `NotImplementedError`; there is no automatic sensor calibration, coordinate mapping or timing loop in this controller.

## Exercises

Supply a second frame and compare values, then supply an empty frame and observe that values remain unchanged. A future live input adapter would need explicit units, coordinate conventions, timestamps and failure handling. This mock exercise does not establish a real rig, data recorder or hardware safety behavior.
