# First Movement

Get your hand moving in under 5 minutes with hardware connected, or 2 minutes in simulation.

Create a file named `hello_hand.py`:

```python
from dexterous_hand import Hand

def main():
    # Use Hand.mock() for simulation, or Hand(driver=HardwareDriver()) for real hardware.
    hand = Hand.mock()
    
    print("Moving joints...")
    hand.move_joints({"thumb_flex": 0.3, "index_flex": 0.4})
    
    for state in hand.read_joints():
        print(f"{state.name}: {state.position_rad:.2f} rad")

if __name__ == "__main__":
    main()
```

Run the script:

```bash
python3 hello_hand.py
```

**Expected Output:**
```
Moving joints...
thumb_flex: 0.30 rad
index_flex: 0.40 rad
...
```
