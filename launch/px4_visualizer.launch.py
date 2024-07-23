from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Define the absolute path to the RViz config
    package_dir = os.path.join(
        get_package_share_directory('px4_ros_visualizer'),
        'config',
        'px4_visualizer_config.rviz'
    )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'rviz_config',
            default_value=package_dir,
            description='Path to RViz config file'
        ),
        Node(
            package='px4_ros_visualizer',
            executable='px4_visualizer',
            name='px4_visualizer',
            output='screen'
        ),
        ExecuteProcess(
            cmd=['rviz2', '-d', LaunchConfiguration('rviz_config')],
            output='screen'
        )
    ])


