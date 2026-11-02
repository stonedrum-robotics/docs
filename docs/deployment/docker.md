# Container source status

The SDK includes `docker/Dockerfile` and `docker/docker-compose.yml`. The Dockerfile starts from `ros:humble-ros-base`, adds pip/colcon tooling, copies the SDK and installs its development extras. The Compose file describes a development service with the repository mounted as a volume.

These source files are not proof of a successful image build, an available image registry, or a preinstalled MoveIt/MuJoCo environment. This Docs repair did not build or run the container, and the Python mock checks do not establish container/device compatibility.

Before using a container as reproducible evidence, record the actual base-image digest, dependency resolution, build result, runtime environment and tested behavior. Hardware access and ROS networking require their own configuration-specific review. Use the standalone [mock source setup](../getting-started/installation.md) for the smaller offline example.
