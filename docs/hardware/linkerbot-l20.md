# Linkerbot L20 & L20 Lite
The Linkerbot L20 and L20 Lite are research-grade dexterous robotic hands designed for advanced manipulation tasks, offering a balance of high degrees of freedom (DOF) and robust linkage-driven kinematics. Built by Stonedrum Robotics, the L20 series is tailored for research laboratories and educational institutions requiring precision grasping, human-like dexterity, and seamless ROS compatibility. The self-developed linkage transmission ensures high rigidity and strong grip force, making it suitable for both complex research experiments and demanding manipulation use cases where tendon-driven systems might lack the required durability.

## Specifications
| Model | DOF | Drive | Weight | Max Load | Interface | Primary Use |
|---|---|---|---|---|---|---|
| **L20 Lite** | 20 (10+10) | Linkage | 800g | 25kg | CAN/RS485 + ROS | Research entry, education |
| **L20** | 21 (16+5) | Linkage | 1100g | 10kg | CAN/RS485 | Research flagship |

*Note: Both models achieve ±0.20mm repositioning accuracy.*

## Pinout Diagram
```text
Linkerbot L20 / L20 Lite Connector Pinout
┌─────────────────────────────────┐
│ Pin 1: Power (V+)               │
│ Pin 2: Ground (GND)             │
│ Pin 3: CAN_H / RS485_A          │
│ Pin 4: CAN_L / RS485_B          │
│ Pin 5: Signal GND               │
│ Pin 6: Shield                   │
│ Pin 7-8: [VENDOR_SPEC_REQUIRED] │
└─────────────────────────────────┘
* Exact voltage, current, fuse, and inrush values are [VENDOR_SPEC_REQUIRED].
```

## Communication Protocol
The L20 and L20 Lite support both CAN and RS-485 interfaces. 
- **CAN**: Operates at 1Mbps using a proprietary protocol.
- **RS-485**: Operates at 115200–256000 bps using Modbus.
Select the appropriate communication interface based on your controller setup. Both interfaces are fully integrated into the ROS 2 environment provided by the SDK.

## Mounting Interface
The mechanical interface requires an adapter plate to mount the hand to standard robot flanges (e.g., ISO 9409-1-50-4-M6). The Linkerbot-side bolt circle, dowel locations, and wrist orientation are `[VENDOR_SPEC_REQUIRED]` and must be referenced from the official mechanical drawings. Ensure the mounting plate is rigid and features a clocking mark to reproduce the hand frame if removed.

## Safety Limits
- Do not exceed the maximum load limits specified above.
- Always operate the hand within the defined input voltage and current specifications (`[VENDOR_SPEC_REQUIRED]`).
- Ensure the communication cable bundle does not tighten or rub during full wrist motion.
- Implement external emergency stops as required by your lab's safety protocol.

**CE Note:** CE certification status is currently under verification — contact info@stonedrum.co for compliance documentation.
