"""Challenge: one command starts the simulation AND my safety monitor.

    ros2 launch my_robot everything.launch.py
    ros2 launch my_robot everything.launch.py stage:=2 min_height:=0.05
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('stage', default_value='1'),
        DeclareLaunchArgument('min_height', default_value='0.03'),

        # Run another launch file, as if you'd typed `ros2 launch workshop_arm workshop.launch.py`.
        IncludeLaunchDescription(
            PathJoinSubstitution([FindPackageShare('workshop_arm'), 'launch', 'workshop.launch.py']),
            launch_arguments={'stage': LaunchConfiguration('stage')}.items(),
        ),

        # ...and our own launch file, passing min_height along.
        IncludeLaunchDescription(
            PathJoinSubstitution([FindPackageShare('my_robot'), 'launch', 'safety.launch.py']),
            launch_arguments={'min_height': LaunchConfiguration('min_height')}.items(),
        ),
    ])
