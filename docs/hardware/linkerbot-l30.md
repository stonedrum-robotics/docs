# Linkerbot L30
The Linkerbot L30 is the flagship dexterous robotic hand from Stonedrum Robotics, engineered for cutting-edge AI and machine learning research. Unlike the linkage-driven L20 series, the L30 features an advanced tendon-driven architecture that closely mimics human hand biomechanics. With 21 degrees of freedom (17 actuated, 4 passive) and an exceptional maximum speed of 440°/s, the L30 is uniquely positioned for reinforcement learning applications where high-speed, biomimetic manipulation is required. Its high-bandwidth CAN FD communication interface enables ultra-low latency control, making it a powerful platform for embodied intelligence and complex teleoperation tasks.

## Specifications
| Model | DOF | Drive | Weight | Max Load | Interface | Primary Use |
|---|---|---|---|---|---|---|
| **L30** | 21 (17+4) | Tendon | 1400g | 2kg | CAN FD (5Mbps) | AI/ML research, biomimetic |

*Note: The L30 achieves ±0.20mm repositioning accuracy.*

## Pinout Diagram
```text
Linkerbot L30 Connector Pinout
┌─────────────────────────────────┐
│ Pin 1: Power (V+)               │
│ Pin 2: Ground (GND)             │
│ Pin 3: CANFD_H                  │
│ Pin 4: CANFD_L                  │
│ Pin 5: Signal GND               │
│ Pin 6: Shield                   │
│ Pin 7-8: [VENDOR_SPEC_REQUIRED] │
└─────────────────────────────────┘
* Exact voltage, current, fuse, and inrush values are [VENDOR_SPEC_REQUIRED].
```

## Communication Protocol
To support its high-speed control requirements, the L30 utilizes CAN FD (Enhanced CAN), capable of speeds up to 5Mbps. This ensures minimal latency when streaming continuous joint trajectories from reinforcement learning policies or teleoperation inputs. Ensure your host system is equipped with a compatible CAN FD interface adapter.

## Mounting Interface
Similar to the L20 series, the L30 requires a custom adapter plate to mate with standard robot flanges. The Linkerbot-side bolt circle, dowel locations, and wrist orientation are `[VENDOR_SPEC_REQUIRED]`. The mounting solution must account for the 1400g mass of the hand when calculating payload and center of gravity on the host arm.

## Safety Limits
- The maximum load is limited to 2kg; do not exceed this limit to prevent damage to the tendon drive system.
- Always operate the hand within the defined input voltage and current specifications (`[VENDOR_SPEC_REQUIRED]`).
- Ensure the communication cable bundle does not tighten or rub during full wrist motion.
- Implement external emergency stops as required by your lab's safety protocol.

**CE Note:** CE certification status is currently under verification — contact info@stonedrum.co for compliance documentation.
