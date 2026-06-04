# Hardware Setup: Linkerbot

This guide covers the physical setup and initial configuration of the Stonedrum Robotics Linkerbot hardware.

## Unboxing Checklist

When you receive your Linkerbot package, please verify that it contains the following items:

*   1x Linkerbot Dexterous Hand Unit
*   1x Power Supply Unit (24V)
*   1x CAN Bus Communication Cable
*   1x USB-to-CAN Adapter
*   Mounting Hardware Kit `[VENDOR_SPEC_REQUIRED]`
*   Quick Start Documentation

If any items are missing or damaged, please contact support at info@stonedrum.co immediately.

## Power Supply Requirements

The Linkerbot requires a stable power source to operate safely and effectively. 

*   **Voltage:** 24V DC
*   **Current:** `[VENDOR_SPEC_REQUIRED]` Amps minimum.

Ensure that the provided power supply or your custom power distribution system meets these specifications. Supplying incorrect voltage or insufficient current can result in erratic behavior or permanent damage to the hardware.

## Communication Connection

The Linkerbot communicates with the host computer via a CAN bus interface.

1.  Connect the CAN bus cable to the connector on the base of the Linkerbot.
2.  Connect the other end of the cable to the provided USB-to-CAN adapter.
3.  Plug the USB-to-CAN adapter into an available USB port on your host computer.

*Note: For detailed pinouts and advanced networking configurations, please refer to the wiring diagram in `linkerbot-l20.md`.*

## First Power-On Sequence

Safety is paramount when working with robotic hardware. Follow this sequence strictly for your first power-on:

1.  **Clear the Area:** Ensure the Linkerbot has a clear workspace. Remove any obstacles or delicate objects from its immediate vicinity.
2.  **Secure Mounting:** Verify that the hand is securely mounted to a stable base or robotic arm flange.
3.  **Visual Inspection:** Inspect all cables for frays or pinches. Ensure the power and CAN connections are fully seated.
4.  **Power On:** Turn on the 24V power supply. You should see the status LEDs on the hand illuminate.
5.  **Do Not Send Commands Yet:** Wait for the boot sequence to complete (usually indicated by a specific LED pattern). Do not attempt to run any SDK scripts immediately.

## Switching from Mock to Hardware Mode

Once the hardware is powered and connected, you need to update your code to interface with it rather than the software simulation.

In your Python scripts, you will transition away from using `Hand.mock()`. Instead, you will instantiate a hardware driver, connect to the specific CAN interface, and pass that driver to the `Hand` class.

*Example (Conceptual):*
```python
# Before (Mock Mode)
# from dexterous_hand import Hand
# hand = Hand.mock()

# After (Hardware Mode)
from dexterous_hand import Hand
from dexterous_hand.driver import HardwareHandDriver # Ensure this is imported

# Replace 'can0' with your actual CAN interface name
driver = HardwareHandDriver(interface='can0')
driver.connect()
hand = Hand(driver=driver)

# Now, hand.move_joints() will move the physical robot.
```

## Compliance Note

**CE certification status is currently under verification — contact info@stonedrum.co for compliance documentation.**
