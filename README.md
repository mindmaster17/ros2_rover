# ros2_rover

ROS 2 based differential drive rover

# 🤖 ROS 2 Humble Docker Environment

Welcome to the ROS 2 Humble Docker workspace! This repository provides a fully configured, containerized development environment for ROS 2.

By using Docker, you can keep your host computer clean and ensure your ROS 2 projects run exactly the same way across different machines. This setup includes built-in support for hardware acceleration (NVIDIA GPUs), GUI application forwarding (like Gazebo or RViz), and WebSocket bridging for external visualizers like Foxglove Studio.

---

## ✨ Features

- **ROS 2 Humble Desktop:** Pre-installed with common packages (Nav2, Gazebo, SLAM Toolbox).
- **Hardware Acceleration:** Configured for NVIDIA GPUs (including Hybrid laptop setups).
- **GUI Support:** Run visual tools like RViz2 and Gazebo directly from the container to your host screen.
- **WebSocket Ready:** Pre-configured `rosbridge-suite` to connect easily with Foxglove Studio or VS Code.
- **Network Patched:** Includes built-in fixes for common Gazebo/ROS 2 multicast discovery issues.

---

## 📋 Prerequisites & Installation

Before running the container, you need to install Docker on your host operating system. Find your OS below:

### 🐧 Debian / Ubuntu

```bash
# Install Docker and Docker Compose
sudo apt update
sudo apt install docker.io docker-compose-v2 x11-xserver-utils

# Add your user to the docker group (so you don't need to type 'sudo' every time)
sudo usermod -aG docker $USER
newgrp docker
```

### 🏹 Arch Linux / CachyOS

```bash
# Install Docker, Docker Compose, and Xhost (for GUI apps)
sudo pacman -S docker docker-compose docker-buildx xorg-xhost

# Enable Docker service
sudo systemctl enable --now docker

# Add your user to the docker group
sudo usermod -aG docker $USER
newgrp docker
```

### 🍓 Raspberry Pi (Raspberry Pi OS / Debian ARM64)

Note: Raspberry Pi does not use NVIDIA GPUs, so the environment will automatically fall back to standard CPU processing.

```bash
# Install Docker via the official script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add your user to the docker group
sudo usermod -aG docker $USER
newgrp docker
```

### 🎮 (Optional) NVIDIA GPU Users (Linux x86_64)

If you have an NVIDIA GPU, install the NVIDIA Container Toolkit so the container can use your graphics card for simulations:

- Ubuntu/Debian: Follow the official NVIDIA docs.
- Arch/CachyOS: `paru -S nvidia-container-toolkit` or `yay -S nvidia-container-toolkit`.

After installing, restart Docker: `sudo systemctl restart docker`.

---

## 🚀 Quick Start Guide

1. **Enable GUI Applications** (Required every time you restart your PC)

   To allow the Docker container to open windows (like Gazebo) on your screen, run this on your host machine:

   ```bash
   xhost +local:docker
   ```

2. **Build the Environment**

   Navigate to this repository's folder in your terminal and build the Docker image. This downloads ROS 2 and installs all the required packages.

   ```bash
   docker compose build
   ```

3. **Start the Container**

   Run the container in the background:

   ```bash
   docker compose up -d
   ```

4. **Enter the Workspace**

   To open a terminal inside your new ROS 2 environment, use this command:

   ```bash
   docker exec -it shadow_rover bash
   ```

   (You are now inside the container! You can run commands like `colcon build` or `ros2 run` here).

---

## 📊 Visualizing Data with Foxglove Studio

This container is designed to work seamlessly with Foxglove Studio for visualizing 3D models, Lidar scans, and camera feeds without heavy GUI tools.

1. Inside the container, start the WebSocket bridge:

   ```bash
   ros2 launch rosbridge_server rosbridge_websocket_launch.xml
   ```

2. On your Host PC, open Foxglove Studio (Desktop App or Web version at [studio.foxglove.dev](https://studio.foxglove.dev)).

3. Click **Open Connection** -> **Rosbridge (WebSocket)**.

4. Enter `ws://localhost:9090` and click connect.

📁 Repository Structure
src/ - Your actual ROS 2 code goes here. This folder is linked directly to the container, so any edits you make on your PC happen instantly inside the container.

Dockerfile - The recipe that builds the ROS 2 environment. You can add more apt install commands here if you need extra packages.

docker-compose.yml - The configuration file that links your hardware, graphics, and network to the container.

tactical_entrypoint.sh - A startup script that runs automatically to fix network routing and load ROS 2 source files.

🛑 Stopping and Cleaning Up
When you are done working, you can stop the container to free up system resources:

Bash
docker compose down
