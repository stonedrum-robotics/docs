# Tutorial 5: Simulation with MuJoCo

Physical hardware can be slow to test and risky during early development. Using MuJoCo allows for rapid prototyping of contact-rich manipulation tasks with high fidelity physics. This tutorial elaborates on `examples/05_sim_mujoco.py`.

## MuJoCo Setup

MuJoCo uses MJCF (MuJoCo XML) formats to define rigid body dynamics, collision meshes, and actuators. To simulate the Stonedrum Robotics hand, you need the official MJCF assets.

Currently, the SDK expects you to place these assets in a shared resource directory.

## Linkerbot MJCF Specifications

The Linkerbot hand requires precise mass and inertia definitions to simulate accurately. However, the exact actuator dynamics, friction coefficients, and tendon routings are vendor-specific.

`[VENDOR_SPEC_REQUIRED]`

Please consult the vendor documentation for the exact Linkerbot hardware specifications required to accurately populate your MJCF `actuator` and `tendon` tags. We do not distribute proprietary CAD or mass matrix data in the open-source SDK.

## Mock Driver Swap

To use the simulation, you must replace the standard SDK hardware driver with a MuJoCo interface bridge. Instead of using `Hand.mock()`, you will map the `Hand.move_joints()` commands to MuJoCo `ctrl` arrays.

A basic swap looks like this:

```python
from dexterous_hand import Hand
import mujoco

# Load model
model = mujoco.MjModel.from_xml_path("path/to/linkerbot.xml")
data = mujoco.MjData(model)

def apply_sim_commands(joint_targets_rad):
    # Map target dictionary to MuJoCo control array based on actuator names
    for name, value in joint_targets_rad.items():
        actuator_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, name)
        data.ctrl[actuator_id] = value

# Assuming a custom Hand subclass for simulation:
# sim_hand = MujocoHand(apply_sim_commands)
```

## Community Models

Because accurate simulation models require vendor specs (`[VENDOR_SPEC_REQUIRED]`), many users rely on community-maintained approximations for initial testing. 

You can find community-contributed MJCF models on platforms like GitHub and the MuJoCo Menagerie. Always verify the physical accuracy of community models against your real hardware before relying on them for fine contact tasks.

For inquiries about official simulation partnerships, email info@stonedrum.co.
