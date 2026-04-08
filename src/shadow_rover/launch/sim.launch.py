import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    # 1. Configuration
    package_name = 'shadow_rover'
    urdf_file_name = 'simple_rover.urdf' # <--- MATCHES YOUR FILENAME

    # 2. Setup Paths
    pkg_share = get_package_share_directory(package_name)
    urdf_path = os.path.join(pkg_share, 'urdf', urdf_file_name)
    gazebo_ros_pkg = get_package_share_directory('gazebo_ros')

    # 3. Process URDF
    doc = xacro.process_file(urdf_path)
    robot_description = {'robot_description': doc.toxml()}

    # 4. Nodes
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    node_spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
arguments=[
            '-topic', 'robot_description',
            '-entity', 'shadow_rover',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '1.0'  # <--- DROP HEIGHT (Meters)
        ],
        output='screen'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_pkg, 'launch', 'gazebo.launch.py')
        ),
    )

    return LaunchDescription([
        gazebo,
        node_robot_state_publisher,
        node_spawn_entity
    ])
