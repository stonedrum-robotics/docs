# Dexterous Hand SDK documentation

Explore Python hand interfaces and an in-memory mock for joint commands, joint states, named grasp data and canned teleoperation frames. This documentation describes the public SDK commit `17d8768affe743e9f997f1df5b100ea782ee5526`.

## Start here

1. Follow [source setup](getting-started/installation.md).
2. Run [the first mock example](getting-started/first-movement.md).
3. Explore [joint control](tutorials/01-basic-control.md), [grasp sequences](tutorials/02-grasp-sequence.md) and the [Hand API](api-reference/hand.md).

The mock stores numbers in memory. It does not simulate contact, force, collisions or device dynamics. Linkerbot and OmniHand adapters reject unsupported hardware operations before transport I/O. The current SDK supplies no physical emergency-stop implementation.

## Other material

The existing ROS 2, simulation, hardware and application routes explain source status and future integration questions. They do not establish working device support, validated procedures or delivered services. Hardware names refer to external products; these pages do not identify Stonedrum as their manufacturer.

For company information, visit [Stonedrum](https://stonedrum.co/). The [catalogue](https://shop.stonedrum.co/) contains product references. General enquiries: [info@stonedrum.co](mailto:info@stonedrum.co).
