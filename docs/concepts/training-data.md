# Training Data

Data scarcity is one of the most significant bottlenecks in training generalized dexterous manipulation policies. Imitation learning and Vision-Language-Action (VLA) models require massive volumes of high-quality human-robot interaction data to learn robust grasping and manipulation strategies.

## The Anatomy of High-Quality Dexterous Data

To be useful for modern AI training, dexterous hand data must be multi-modal and highly synchronized. A comprehensive dataset typically includes:

*   **Hand Pose Kinematics:** High-precision tracking of joint angles (e.g., 20+ degrees of freedom) over time.
*   **Tactile Sensing:** High-density contact data capturing force, slip, and deformation during object interaction.
*   **Vision:** Synchronized RGB, Depth, and Point Cloud streams capturing the environment and the object.
*   **Annotations:** Task-level and atomic action-level annotations (often in natural language) to provide semantic context for the recorded trajectories.

Furthermore, this data must be packaged in standardized interchange formats (such as HDF5 or those compatible with LeRobot) to ensure frictionless ingestion into machine learning pipelines.

## Integration with the Stonedrum SDK

The Stonedrum SDK is evolving to address this data bottleneck directly. Our upcoming Training Data Module (`dexterous_hand.data`) will allow researchers to load third-party and partner training datasets directly into their PyTorch or LeRobot workflows.

Because the data module integrates with the same unified `Hand` abstraction used for hardware control, policies trained on these datasets can map cleanly onto any supported hardware (such as Linkerbot or AGILINK hands). This eliminates the need for complex, custom kinematic retargeting scripts.

## Data Governance and GDPR

As a European entity, Stonedrum Robotics is building this module with EU data protection requirements in mind from the start. Collecting and distributing high-fidelity human interaction data often touches upon behavioral biometrics and privacy regulations. Our platform ensures that any datasets distributed through our service meet stringent GDPR compliance standards, providing a secure, legally compliant data gateway for EU research labs and corporate R&D. This stands as a key differentiator compared to raw, unregulated data sources.

## Status

The `dexterous_hand.data` module is currently **in development**, with a targeted release for Q4 2026. 

Interested in early access or want to discuss data partnership opportunities? Contact `info@stonedrum.co`.
