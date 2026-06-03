# Safety Constraints

To protect both operators and hardware, several safety constraints are enforced at the driver level:

- **Position Limits**: Hard stops in firmware prevent hyperextension.
- **Velocity Limits**: Max joint velocities are clamped.
- **Torque/Current Limits**: Overcurrent protection automatically shuts down the motor if an obstacle is hit.
- **Emergency Stop**: The hardware includes an E-Stop circuit.

**Note**: CE certification status is currently under verification — please contact Stonedrum Robotics for the latest compliance documentation.
