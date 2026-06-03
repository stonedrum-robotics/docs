# Docker Deployment

We provide a Dockerfile and `docker-compose.yml` to isolate the ROS 2 environment.

```bash
cd dexterous-hand-sdk/docker
docker-compose up -d
docker-compose exec ros2_env bash
```

This ensures all dependencies (ROS 2, MoveIt 2, MuJoCo) are pre-installed.
