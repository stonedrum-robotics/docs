# Grasp vocabulary and mock target sets

Power and precision grasps provide a useful vocabulary for discussing manipulation. A power grasp emphasizes broad support/contact, while a precision grasp emphasizes more localized finger contact. This vocabulary does not establish the result of a physical experiment.

## The source library

The pinned `GraspLibrary.default_poses()` contains nine primary entries and three compatibility entries (`open`, `pinch`, `cylindrical`), twelve entries total. The target dictionaries below are software example values in radians, not calibrated hardware poses or safe object-handling instructions.

| Entry | Stored targets |
|---|---|
| `relaxed_open` | thumb_flex=0.08, index_flex=0.08, middle_flex=0.08, ring_flex=0.08, little_flex=0.08 |
| `precision_pinch` | thumb_flex=0.65, index_flex=0.7, middle_flex=0.12, ring_flex=0.08, little_flex=0.08 |
| `tripod` | thumb_flex=0.7, index_flex=0.65, middle_flex=0.62, ring_flex=0.18, little_flex=0.18 |
| `lateral_pinch` | thumb_flex=0.72, index_flex=0.38, middle_flex=0.22, ring_flex=0.18, little_flex=0.18 |
| `index_point` | thumb_flex=0.42, index_flex=0, middle_flex=0.82, ring_flex=0.84, little_flex=0.86 |
| `cylindrical_power` | thumb_flex=0.55, index_flex=0.9, middle_flex=0.9, ring_flex=0.9, little_flex=0.9 |
| `spherical_power` | thumb_flex=0.62, index_flex=0.78, middle_flex=0.82, ring_flex=0.78, little_flex=0.72 |
| `hook` | thumb_flex=0.05, index_flex=1.05, middle_flex=1.08, ring_flex=1.08, little_flex=1.02 |
| `platform` | thumb_flex=0.18, index_flex=0.05, middle_flex=0.05, ring_flex=0.05, little_flex=0.05 |
| `open` | Empty dictionary; leaves existing mock values unchanged |
| `pinch` | thumb_flex=0.65, index_flex=0.7, middle_flex=0.12, ring_flex=0.08, little_flex=0.08 |
| `cylindrical` | thumb_flex=0.55, index_flex=0.9, middle_flex=0.9, ring_flex=0.9, little_flex=0.9 |

`pinch` has the same targets as `precision_pinch`; `cylindrical` has the same targets as `cylindrical_power`. Despite its historical name, `open` does not map to `relaxed_open`: it carries `{}`. Use `Hand.open()` when a mock exercise needs zero targets.

## Inspecting and customizing values

```python
from dexterous_hand import Hand
from dexterous_hand.grasp_library import GraspPose

hand = Hand.mock()
pose = hand.grasps.get("tripod")
print(pose.joint_positions_rad)
custom = GraspPose("custom", {"index_flex": 0.3}, "Mock exercise")
hand.move_joints(custom.joint_positions_rad)
```

`GraspPose` describes a named target dictionary. It does not add force control, object sensing or geometry validation. Continue with the [sequence tutorial](../tutorials/02-grasp-sequence.md).
