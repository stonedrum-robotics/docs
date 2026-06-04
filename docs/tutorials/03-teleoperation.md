# Tutorial 3: Teleoperation

Teleoperation involves controlling a robot in real-time using human input. The Stonedrum Robotics SDK provides a robust `TeleoperationController` to standardize inputs from VR gloves, keyboards, or joysticks. This tutorial walks through `examples/03_teleoperation_keyboard.py`.

## Annotated Walkthrough

Here is the example code:

```python
"""Keyboard teleoperation placeholder."""

from dexterous_hand import Hand
from dexterous_hand.teleoperation import TeleoperationController, TeleoperationFrame

def main() -> None:
    """Apply a canned teleoperation frame in mock mode."""
    # Mock mode keeps the example deterministic and hardware-free.
    hand = Hand.mock()
    
    # The controller owns the translation from frames to Hand.move_joints calls.
    controller = TeleoperationController(hand)
    
    # This canned frame stands in for a keyboard event that curls thumb and index.
    controller.apply_frame(TeleoperationFrame({"thumb_flex": 0.5, "index_flex": 0.5}, "keyboard"))
    
    # In a real keyboard loop, this print would be replaced by live status feedback.
    print("Applied keyboard teleoperation frame")

if __name__ == "__main__":
    main()
```

### TeleoperationController and `read_glove_frame`

The `TeleoperationController` is responsible for receiving normalized `TeleoperationFrame` objects and applying them safely to the hand driver. A `TeleoperationFrame` is simply a dictionary of joint targets coupled with a string identifying the source of the data.

If you inspect the `teleoperation.py` file, you will notice a method called `read_glove_frame()` that currently raises a `NotImplementedError("Glove device integration is vendor-specific.")`. 

Why is this not implemented? VR gloves and motion tracking hardware vary wildly between vendors. A Sensable glove outputs entirely different telemetry formats than an Oculus hand-tracking system. Stonedrum Robotics provides the structured `TeleoperationFrame` so that you can easily write a vendor-specific parser that maps raw glove sensor values into our standard radian format, ensuring hardware flexibility without rewriting the core SDK logic.

### Keyboard Controls Table

If you were to expand this script to listen to live keyboard events (e.g., using the `pynput` library or standard terminal curses), a common keymapping structure would look like this:

| Key | Action             | Target Joint   | Radian Value |
|-----|--------------------|----------------|--------------|
| `W` | Open Index Finger  | `index_flex`   | `0.0`        |
| `S` | Close Index Finger | `index_flex`   | `1.5`        |
| `E` | Open Middle Finger | `middle_flex`  | `0.0`        |
| `D` | Close Middle Finger| `middle_flex`  | `1.5`        |
| `Space`| Open Hand       | All            | `0.0`        |

You would map keyboard events to generate a `TeleoperationFrame`, and then pass that frame into `controller.apply_frame()`.

If you need assistance integrating a specific vendor's VR glove, please reach out to info@stonedrum.co.
