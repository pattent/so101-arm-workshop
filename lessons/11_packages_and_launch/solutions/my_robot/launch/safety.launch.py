"""Start the safety monitor.

    ros2 launch my_robot safety.launch.py
    ros2 launch my_robot safety.launch.py min_height:=0.05
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # A launch argument: something you can set on the command line (min_height:=0.05).
        DeclareLaunchArgument('min_height', default_value='0.03'),

        # Start one node. Same as `ros2 run my_robot safety_monitor`, plus the parameter.
        Node(
            package='my_robot',
            executable='safety_monitor',
            parameters=[{'min_height': LaunchConfiguration('min_height')}],
            output='screen',
        ),
    ])
