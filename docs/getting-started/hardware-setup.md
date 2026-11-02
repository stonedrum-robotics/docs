# Hardware setup status

The published SDK has no working vendor hardware driver. There is no `HardwareHandDriver` class in `dexterous_hand.driver`; Linkerbot and OmniHand adapter operations raise `NotImplementedError` before transport I/O. This page therefore supplies no power-on, pinout, wiring or first-motion procedure.

## Information needed for a future integration

Record the exact manufacturer, product variant, controller and firmware. Obtain their corresponding manufacturer documentation for electrical ratings, connectors, protocol, mounting and emergency-stop behavior. Assign a configuration-specific engineering and safety review before defining any physical test.

Those facts cannot be inferred from a generic Python interface, a product name or a placeholder value. Stonedrum's published mock code does not establish a conformity assessment, responsibility for a manufacturer's documentation, or device compatibility.

Continue with [offline joint updates](first-movement.md). Preliminary [hardware resource notes](https://github.com/stonedrum-robotics/hardware-resources) are investigation inputs, not commissioning clearance.
