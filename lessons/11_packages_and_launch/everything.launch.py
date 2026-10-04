"""Challenge: one command that starts the simulation AND your safety monitor.

Copy this into src/my_robot/launch/, finish it, rebuild, then:
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

        # Run another package's launch file, as if you'd typed
        # `ros2 launch workshop_arm workshop.launch.py stage:=...`
        IncludeLaunchDescription(
            PathJoinSubstitution([FindPackageShare('workshop_arm'), 'launch', 'workshop.launch.py']),
            launch_arguments={'stage': LaunchConfiguration('stage')}.items(),
        ),

        # TODO 1: Include YOUR safety.launch.py the same way (package 'my_robot').
        # TODO 2: Add a min_height launch argument here too, and pass it along to
        #         safety.launch.py in launch_arguments.
    ])
