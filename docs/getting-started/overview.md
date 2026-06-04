# Overview

Welcome to the Stonedrum Robotics platform! This guide will introduce you to our ecosystem and help you get started with your new robotic hand.

## What is a Dexterous Robotic Hand?

A dexterous robotic hand is an advanced end-effector designed to closely mimic the form, function, and kinematic complexity of a human hand. Unlike traditional parallel-jaw grippers or basic suction cups that rely on simple open/close mechanisms, a dexterous hand features multiple articulated fingers, each with several joints. This biomimetic design allows for intricate manipulation of objects of varying shapes, sizes, and fragility, enabling robots to perform tasks in environments designed for humans.

## The Advantage of 20+ Degrees of Freedom (DOF)

Traditional grippers are sufficient for repetitive pick-and-place tasks, but they fall short in complex, unstructured environments. A dexterous hand with 20 or more Degrees of Freedom (DOF) provides significant advantages for advanced research and application:

1. **In-Hand Manipulation:** With 20+ DOF, the hand can reposition and reorient objects without needing to set them down. This is critical for tasks like tool use, where an object must be grasped and then adjusted for optimal grip before use.
2. **Conformal Grasping:** The high degree of articulation allows the fingers to wrap completely around irregularly shaped objects. This maximizes contact area, distributing force evenly to safely grasp fragile items or securely hold heavy, uneven loads.
3. **Complex Gesturing and Haptic Exploration:** A multi-DOF hand can execute precise gestures and perform detailed haptic exploration. Researchers can use it to map surfaces, identify object properties by touch, or perform delicate operations requiring fine motor control that simpler grippers simply cannot achieve.

## The Stonedrum Robotics Platform

The Stonedrum Robotics platform provides a complete solution for dexterous manipulation research and development. It consists of:

*   **Hardware (Linkerbot):** Our state-of-the-art dexterous hand hardware, engineered for durability and precision.
*   **Dexterous Hand SDK:** A robust Python SDK (`dexterous_hand`) providing a high-level API for commanding the hand, managing grasps, and reading joint states.
*   **ROS2 Integration:** Full support for ROS2 (Humble), allowing seamless integration into broader robotics ecosystems and complex control architectures.
*   **Local Support:** Dedicated support from the Stonedrum Robotics team to ensure your success. Contact us at info@stonedrum.co.

## Mock Mode vs. Hardware Mode

The SDK is designed to be highly flexible, offering two primary modes of operation:

*   **Mock Mode:** Use this mode when you want to test your code, develop grasping strategies, or run simulations without having the physical hardware connected. It creates a simulated hand (`Hand.mock()`) that responds to API calls exactly like the real device, making it perfect for CI/CD pipelines and offline development.
*   **Hardware Mode:** Use this mode when you are ready to deploy your algorithms to the physical Linkerbot hand. It interfaces directly with the hardware driver to execute movements in the real world.

## Next Steps

Ready to get started? Head over to the [Installation Guide](./installation.md) to set up your development environment.
