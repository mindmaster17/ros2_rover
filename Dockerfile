
# 1. Base Image
FROM osrf/ros:humble-desktop

# 2. Hardware Acceleration Hooks (Ready for any NVIDIA system)
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=graphics,utility,compute

# 3.Pre-installed during the build
RUN apt-get update && apt-get install -y \
    ros-humble-xacro \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-robot-localization \
    ros-humble-rosbridge-suite \
    nano \
    git \
    python3-colcon-common-extensions \
    mesa-utils \
    && rm -rf /var/lib/apt/lists/*

# 4. Quality of Life
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# 5. Drop Zone
WORKDIR ~/ros2_rover
