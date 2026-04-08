# 1. Base Image (The foundation)
FROM osrf/ros:humble-desktop

# 2. Install Tactical Packages (The Arsenal)
# We combine update and install to keep the image clean
RUN apt-get update && apt-get install -y \
    ros-humble-xacro \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-robot-localization \
    nano \
    git \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# 3. Quality of Life Improvements
# Automatically source ROS when you open a terminal
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
