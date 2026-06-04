# Changelog

All notable changes to the Dexterous Hand SDK will be documented in this file.

## [v0.1.0] - Initial Release

### Added
- **Core SDK**: Introduced the base Python API for controlling the L20 dexterous hand.
- **MockHandDriver**: Implemented software-in-the-loop mock mode for offline testing and safe evaluation.
- **GraspLibrary**: Shipped 12 pre-configured Cutkosky-inspired grasp poses (e.g., `tripod`, `cylindrical_power`, `precision_pinch`).
- **ROS 2 Integration**: Provided initial ROS 2 nodes for joint state publishing and command subscription.
- **Docker Support**: Added robust Dockerfiles for containerized development and deployment.
- **CI/CD**: Established automated testing and linting pipelines via GitHub Actions.
