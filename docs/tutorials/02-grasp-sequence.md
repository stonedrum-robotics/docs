# Tutorial 2: Grasp Sequences

Manipulating a dexterous hand joint-by-joint is tedious. To simplify manipulation tasks, the Stonedrum Robotics SDK includes a Grasp Library that maps named poses to specific joint configurations. In this tutorial, we will walk through `examples/02_grasp_sequence.py`.

## Annotated Walkthrough

Let's examine the code:

```python
"""Run a simple grasp sequence."""

# The Hand class exposes named grasps through its built-in GraspLibrary.
from dexterous_hand import Hand

def main() -> None:
    """Move through open, pinch, cylindrical, and open poses."""
    # Use mock mode first; swap in a hardware driver only after safety checks.
    hand = Hand.mock()
    
    # The sequence starts and ends open so a demo begins from a safe posture.
    for grasp in ["open", "pinch", "cylindrical", "open"]:
        # Named grasps expand to joint targets inside dexterous_hand/grasp_library.py.
        hand.move_to_grasp(grasp)
        
        # Printing each step makes the sequence easy to follow in a terminal demo.
        print(f"Applied grasp: {grasp}")

if __name__ == "__main__":
    main()
```

### Cutkosky Poses Explained

The grasps built into the SDK are heavily inspired by the **Cutkosky Grasp Taxonomy**, a standard classification system in robotics for human hand grasping. 
- **`open`**: All joints are extended. This is the resting, safe pose used to approach an object.
- **`pinch`**: The thumb and index finger form a precision grip, useful for picking up small items like screws or coins.
- **`cylindrical`**: The fingers wrap uniformly to grip curved, tubular objects like a pipe or a bottle.

By using these named poses, your application logic becomes much easier to read and maintain. The SDK's `GraspLibrary` handles the complex math of mapping these high-level concepts into exact radian values for every individual joint on the Linkerbot hand.

### Expected Output

If you run the script, you should see the following output in your terminal:
```text
Applied grasp: open
Applied grasp: pinch
Applied grasp: cylindrical
Applied grasp: open
```
Because this uses `Hand.mock()`, the hardware will not move, but the internal state of the driver will update instantly.

## Exercises

1. **Add a Delay**: Import the Python `time` module and add a `time.sleep(1.0)` between each grasp to simulate the time it takes for the hand to physically move.
2. **Print Joint Telemetry**: After applying a grasp, call `hand.read_joints()` and print the position of the `index_flex` joint to observe how different grasps affect specific fingers.
3. **Explore the Library**: Look at the source code in `dexterous_hand/grasp_library.py` (if available) to find other named grasps and add them to the loop.

For help expanding the grasp library, contact info@stonedrum.co.
