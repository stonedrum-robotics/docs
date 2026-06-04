# Your First Movement

In this tutorial, you will write your first script to interact with the Dexterous Hand SDK. 

## Understanding Mock Mode

Before we connect physical hardware, we will use **Mock Mode**. The SDK's mock interface creates a software simulation of the hand that responds to API commands identically to the real hardware. 

Using Mock Mode is crucial for several reasons:
1.  **Safety:** It allows you to test logic and movement sequences without risking damage to the physical hand or surrounding environment.
2.  **Convenience:** You can develop and debug code anywhere, even when the hardware is not available.
3.  **Verification:** It ensures your software environment is correctly configured before introducing hardware complexities.

## The Code

Let's write a simple script to initialize the mock hand and read its starting joint positions. Create a file named `first_movement.py` and add the following code:

```python
# Import the Hand class from the SDK
from dexterous_hand import Hand

# Initialize a mock hand instance. This connects to a simulated driver
# using the default joint configuration.
hand = Hand.mock()

# Read the current state of all joints from the mock driver
joints = hand.read_joints()

# Iterate through the returned joint states and print their names and positions
for joint in joints:
    print(f"Joint: {joint.name}, Position: {joint.position_rad} rad")
```

Run the script:

```bash
python first_movement.py
```

## Understanding the Output

When you execute the script, you should see output similar to this:

```text
Joint: thumb_flex, Position: 0.0 rad
Joint: index_flex, Position: 0.0 rad
Joint: middle_flex, Position: 0.0 rad
Joint: ring_flex, Position: 0.0 rad
Joint: little_flex, Position: 0.0 rad
```

*   **Joint:** This identifies the specific articulation point on the hand. By default, the mock driver initializes five joints representing the primary flexion axes of the thumb, index, middle, ring, and little fingers.
*   **Position:** This is the current angle of the joint, measured in radians (`rad`). Because we just initialized the mock hand and haven't commanded any movement, all positions are `0.0`, representing a neutral, open pose.

## Next Steps

Now that you have successfully initialized the hand and read its state, you are ready to command movements. Proceed to the [Hardware Setup](./hardware-setup.md) to connect your Linkerbot, or continue exploring the SDK in the Grasp Sequence Tutorial.
