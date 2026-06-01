# First Steps

Run the SDK in mock mode before using hardware:

```python
from dexterous_hand import Hand

hand = Hand.mock()
hand.move_to_grasp("pinch")
hand.open()
```

Mock mode validates client code without moving actuators.
