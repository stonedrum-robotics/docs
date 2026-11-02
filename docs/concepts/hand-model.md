# Hand and joint data model

`Hand.mock()` uses the software joint names `thumb_flex`, `index_flex`, `middle_flex`, `ring_flex` and `little_flex`. These five names do not describe the full kinematic structure or degrees of freedom of any named hardware product.

## State and commands

`JointState` contains `name`, `position_rad`, `velocity_rad_s` and `effort_nm`. The mock returns stored position values; velocity and effort remain their default zero values. They are not sensor measurements. A position command is a dictionary mapping known joint names to values in radians; unknown names raise `KeyError` in the mock.

## Configured range checks

`Finger` holds ordered joint names and lower/upper ranges. Its `validate_positions()` checks the supplied list length and values against those configured ranges. That method is separate from `Hand.move_joints()`; the mock command path does not automatically call it. These checks do not establish collision avoidance, physical joint protection or a safety-rated controller.

See the [Finger API](../api-reference/finger.md) and [control behavior](control-modes.md) for the exact software interfaces.
