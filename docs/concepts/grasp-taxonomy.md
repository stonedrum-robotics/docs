# Grasp Taxonomy

Named grasps are foundational for establishing common vocabularies in manipulation research. Standardizing these poses across the Dexterous Hand SDK ensures high reproducibility when evaluating grasping algorithms, sharing benchmark datasets, and comparing research outcomes.

## The Grasp Library

The `GraspLibrary` includes 12 predefined grasp poses, inspired by established robotic taxonomies.

| Grasp Name | Description | Typical Object | Joint Angle Range (rad) |
|------------|-------------|----------------|--------------------------|
| `relaxed_open` | Slightly open rest posture for transport and inspection. | None (Idle) | ~0.08 |
| `precision_pinch` | Thumb and index fingertip contact. | Pegs, beads | 0.08 - 0.70 |
| `tripod` | Three-point precision grasp. | Pens, markers | 0.18 - 0.70 |
| `lateral_pinch` | Thumb pad against the side of the index finger. | Cards, keys | 0.18 - 0.72 |
| `index_point` | Index finger extended, others curled. | Buttons, screens | 0.00 - 0.86 |
| `cylindrical_power`| Power grasp wrapping all fingers. | Handles, bottles | 0.55 - 0.90 |
| `spherical_power` | Spread-finger power grasp. | Balls, knobs | 0.62 - 0.82 |
| `hook` | Fingers curled without thumb opposition. | Bags, handles | 0.05 - 1.08 |
| `platform` | Flat extended-finger support posture. | Trays | ~0.05 |
| `open` | Alias for `relaxed_open`. | None (Idle) | N/A |
| `pinch` | Alias for `precision_pinch`. | Pegs, beads | N/A |
| `cylindrical` | Alias for `cylindrical_power`. | Handles, bottles | N/A |

## Cutkosky Taxonomy Overview

The grasp poses are heavily inspired by the Cutkosky grasp taxonomy (Cutkosky 1989), a seminal work in robotics. The taxonomy fundamentally divides grasps into two main branches:
- **Power Grasps**: Emphasize stability and force. The object is typically held firmly against the palm and the palmar surfaces of the fingers (e.g., `cylindrical_power`, `spherical_power`).
- **Precision Grasps**: Emphasize dexterity and sensitivity. The object is held with the tips of the fingers and thumb, allowing for fine manipulation (e.g., `precision_pinch`, `tripod`).

## Using the Grasp Library

You can easily retrieve a predefined pose from the library and command the hand:

```python
from dexterous_hand.hand import Hand

hand = Hand.mock()
# Retrieve the grasp definition
tripod_pose = hand.grasps.get("tripod")

# Command the hand to move to the grasp
hand.move_to_grasp("tripod")
```

## Defining Custom Poses

For specialized tasks, you can define custom grasp poses and integrate them into your workflow:

```python
from dexterous_hand.grasp_library import GraspPose

custom_pose = GraspPose(
    name="custom_pinch",
    joint_positions_rad={
        "thumb_flex": 0.5,
        "index_flex": 0.5,
        "middle_flex": 0.0,
        "ring_flex": 0.0,
        "little_flex": 0.0,
    },
    description="A moderate pinch for fragile objects."
)

# Command the custom positions directly
hand.move_joints(custom_pose.joint_positions_rad)
```

**Research Citation Note**: If utilizing these standard poses in academic work, consider referencing the foundational taxonomy: *Cutkosky, M. R. (1989). On grasp choice, grasp models, and the design of hands for manufacturing tasks. IEEE Transactions on Robotics and Automation, 5(3), 269-279.*
