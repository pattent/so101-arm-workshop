"""Start the workshop simulation for the stage you're at.

    ros2 launch workshop_arm workshop.launch.py stage:=1   # just the arm (Modules 0-9)
    ros2 launch workshop_arm workshop.launch.py stage:=2   # + bins and blocks at known spots (Module 10)
    ros2 launch workshop_arm workshop.launch.py stage:=3   # + random blocks, live camera, detector (11-12)

Options:
    blocks:=8          how many random blocks in stage 3
    seed:=42           same random layout every time
    camera:=true       turn the camera on in stage 1 or 2 (it's on by default in stage 3)
    detector:=false    in stage 3, don't run our block detector (use yours instead!)
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def setup(context):
    def arg(name):
        return LaunchConfiguration(name).perform(context)

    stage = int(arg('stage'))
    camera = arg('camera') == 'true' if arg('camera') else stage >= 3
    detector = arg('detector') == 'true' if arg('detector') else stage >= 3

    # Stage 1+: the arm, its controllers, MoveIt and RViz.
    actions = [IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('so101_bringup'), 'launch',
                              'follower_moveit_demo.launch.py']),
        launch_arguments={'hardware_type': 'mock'}.items(),
    )]

    # Stage 2: bins and blocks at known spots. Stage 3: blocks at random spots.
    if stage == 2:
        layout = ['known']
    elif stage >= 3:
        layout = ['random', arg('blocks')] + ([arg('seed')] if arg('seed') else [])
    if stage >= 2:
        actions.append(Node(package='workshop_arm', executable='spawn_blocks',
                            arguments=layout, output='screen'))

    if camera:
        actions.append(Node(package='workshop_arm', executable='sim_camera', output='screen'))
    if detector:
        actions.append(Node(package='workshop_arm', executable='block_detector', output='screen'))
    if camera:
        topic = '/vision/debug_image' if detector else '/camera/image_raw'
        actions.append(Node(package='rqt_image_view', executable='rqt_image_view',
                            arguments=[topic]))
    return actions


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('stage', default_value='1', description='1, 2 or 3'),
        DeclareLaunchArgument('blocks', default_value='5'),
        DeclareLaunchArgument('seed', default_value=''),
        DeclareLaunchArgument('camera', default_value=''),
        DeclareLaunchArgument('detector', default_value=''),
        OpaqueFunction(function=setup),
    ])
