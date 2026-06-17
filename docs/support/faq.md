# Frequently Asked Questions (FAQ)

**1. What is the Dexterous Hand SDK?**
The Dexterous Hand SDK is a Python library provided by Stonedrum Robotics to control and interface with the L20 dexterous hand.

**2. Which Python versions are supported?**
The SDK requires Python 3.10 or newer (3.10, 3.11, and 3.12 are tested in CI).

**3. What operating systems are supported?**
We officially support Ubuntu Linux and macOS. Windows is supported via WSL2.

**4. Which ROS 2 distributions are supported?**
We currently support ROS 2 Humble (Ubuntu 22.04) and ROS 2 Jazzy (Ubuntu 24.04).

**5. Can I use the SDK without ROS 2?**
Yes, the core `dexterous_hand` Python package is completely independent of ROS 2 and can be run standalone.

**6. Can I simulate the hand without physical hardware?**
Yes. You can use the built-in Mock Mode for software-in-the-loop testing, or use our provided URDF models in simulators like Gazebo or MuJoCo.

**7. How do I enable Mock Mode?**
Simply initialize the hand using the mock factory method: `hand = Hand.mock()`. This requires no physical connection.

**8. How do I define a custom grasp pose?**
You can instantiate a `GraspPose` object with your desired joint angles and pass the `joint_positions_rad` dictionary directly to `hand.move_joints()`.

**9. What are the standardized joint names?**
The 5 main joints used in the SDK are `thumb_flex`, `index_flex`, `middle_flex`, `ring_flex`, and `little_flex`.

**10. Is MoveIt 2 supported?**
MoveIt 2 configuration packages are in development and will be provided in a future release to enable advanced motion planning.

**11. Does the hand require manual calibration?**
Under normal operation, the hand auto-calibrates upon startup. Manual calibration is only required if an actuator is replaced.

**12. Why do I see a `NotImplementedError` in `read_glove_frame`?**
Teleoperation via data gloves is planned for a future update. The method signature exists but is not yet implemented.

**13. Is the hardware CE certified?**
The CE certification is currently **under verification**. For more details, please contact info@stonedrum.co.

**14. How do I report a bug or request a feature?**
Please use the GitHub Issues tracker on our repository to report bugs or submit feature requests.

**15. Who do I contact for commercial enquiries?**
For enterprise support, volume pricing, or general commercial enquiries, please contact Stonedrum Robotics at info@stonedrum.co.
