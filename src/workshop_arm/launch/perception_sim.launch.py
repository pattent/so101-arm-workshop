"""Start everything for the perception demo: the simulated arm + MoveIt + RViz,
the overhead camera, the block detector, and a window showing what the camera sees.

    ros2 launch workshop_arm perception_sim.launch.py
"""

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    robot = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('so101_bringup'), 'launch',
                              'follower_moveit_demo.launch.py']),
        launch_arguments={'hardware_type': 'mock'}.items(),
    )
    camera = Node(package='workshop_arm', executable='sim_camera', output='screen')
    detector = Node(package='workshop_arm', executable='block_detector', output='screen')
    viewer = Node(package='rqt_image_view', executable='rqt_image_view',
                  arguments=['/vision/debug_image'])
    return LaunchDescription([robot, camera, detector, viewer])
