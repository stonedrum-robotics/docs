# Basic Control

Use mock mode for the first control loop:

```python
from dexterous_hand import Hand

hand = Hand.mock()
hand.move_joints({"thumb_flex": 0.2, "index_flex": 0.3})
```
