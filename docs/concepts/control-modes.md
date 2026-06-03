# Control Modes

The SDK and firmware support multiple control paradigms to suit different research needs.

- **Position Control**: Direct joint angle commands (default).
- **Torque Control**: Commanded joint efforts, essential for compliant manipulation and reinforcement learning.
- **Impedance Control**: Virtual spring-damper behavior at the joint level.

Check the `driver` documentation to see how to switch modes.
