import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    # 1. The Micro-ROS Agent (Talks to ESP32)
    # We assume you have the agent installed in the Docker container
    micro_ros_agent = Node(
        package='micro_ros_agent',
        executable='micro_ros_agent',
        name='micro_ros_agent',
        arguments=['serial', '--dev', '/dev/ttyUSB0', '-v6'],
        output='screen'
    )

    # 2. Dummy Message (To prove it works)
    # tactical_check = ExecuteProcess(
    #     cmd=['echo', 'Shadow Protocol Initiated: Rover Systems Online'],
    #     output='screen'
    # )

return LaunchDescription([
    # micro_ros_agent,  <-- REMOVE or COMMENT THIS
    ExecuteProcess(
        cmd=['echo', 'Shadow Protocol: Rover Systems Standing By'],
        output='screen'
    )
])
