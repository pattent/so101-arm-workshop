"""Exercise 4: your first launch file. Copy this into src/my_robot/launch/ to use it.

When it's finished:
    ros2 launch my_robot safety.launch.py
    ros2 launch my_robot safety.launch.py min_height:=0.05

A launch file is a Python file with one job: generate_launch_description() returns a list
of things to start. ROS then starts them all, and Ctrl+C stops them all.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Start one node. This does the same as typing `ros2 run my_robot hello`.
        Node(package='my_robot', executable='hello', output='screen'),

        # TODO 1: Replace the hello node with your safety_monitor node.

        # TODO 2: Declare a launch argument, so min_height can be set on the command line:
        #             DeclareLaunchArgument('min_height', default_value='0.03'),
        #         and pass it to the node as a parameter, by adding this inside Node(...):
        #             parameters=[{'min_height': LaunchConfiguration('min_height')}],
    ])
