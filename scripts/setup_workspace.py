"""Download the SO-101 robot packages and adapt them for the workshop.

Run inside `pixi shell` with:  python scripts/setup_workspace.py
Works the same on Windows, macOS and Linux.
"""

import subprocess
from pathlib import Path

REPO_URL = 'https://github.com/esol-community/so101-ros-physical-ai.git'
REPO_COMMIT = '58318c905a2c61289fa907de85cb8473322fbe68'  # tested 2026-10-03

ROOT = Path(__file__).resolve().parent.parent
REPO_DIR = ROOT / 'src' / 'so101-ros-physical-ai'

# Packages we don't need for simulation lessons (cameras, LeRobot, real-servo driver).
SKIP_PACKAGES = [
    'episode_recorder',
    'rosbag_to_lerobot',
    'so101_camera_calibration',
    'so101_inference',
    'so101_kinematics',
    'so101_kinematics_msgs',
    'so101_teleop',
    'feetech_ros2_driver',
]

# Packages we build: robot model, MoveIt config, launch files.
BUILD_PACKAGES = ['so101_description', 'so101_moveit_config', 'so101_bringup']

# pick_ik (the upstream IK solver) is Linux-only, so use KDL, which ships with
# MoveIt on every platform. Position-only IK suits a 5-joint arm.
KINEMATICS_YAML = """\
# Workshop change: KDL ships with MoveIt on Linux, macOS and Windows
# (pick_ik is Linux-only on RoboStack).
manipulator:
  kinematics_solver: kdl_kinematics_plugin/KDLKinematicsPlugin
  kinematics_solver_search_resolution: 0.005
  kinematics_solver_timeout: 0.2
  kinematics_solver_attempts: 10
  # 5-DOF arm: solve for gripper position only, so "move_to(x, y, z)" just works.
  position_only_ik: true
"""


def git(*args, cwd=None):
    subprocess.run(['git', *args], cwd=cwd, check=True)


def main():
    if not REPO_DIR.exists():
        print('Downloading the SO-101 robot packages...')
        git('clone', REPO_URL, str(REPO_DIR))
    git('checkout', '--quiet', REPO_COMMIT, cwd=REPO_DIR)

    for name in SKIP_PACKAGES:
        package_dir = REPO_DIR / name
        if package_dir.exists():
            (package_dir / 'COLCON_IGNORE').touch()

    (REPO_DIR / 'so101_moveit_config' / 'config' / 'kinematics.yaml').write_text(KINEMATICS_YAML)

    # These packages hold only models and config files. Telling CMake they use no
    # programming language means no C++ compiler is needed (no Visual Studio on Windows).
    for name in BUILD_PACKAGES:
        cmake_file = REPO_DIR / name / 'CMakeLists.txt'
        text = cmake_file.read_text()
        if 'LANGUAGES NONE' not in text:
            cmake_file.write_text(text.replace(f'project({name})', f'project({name} LANGUAGES NONE)'))
    # Don't endlessly replay the last planned motion in RViz (confusing for beginners).
    rviz_file = REPO_DIR / 'so101_moveit_config' / 'config' / 'moveit.rviz'
    rviz_file.write_text(rviz_file.read_text().replace('Loop Animation: true', 'Loop Animation: false'))

    # Windows fix: the xacro command wraps camera poses in single quotes, which only
    # Linux/macOS treat as grouping. Double quotes work on every platform.
    for launch_name in ['follower.launch.py', 'follower_split.launch.py']:
        launch_file = REPO_DIR / 'so101_bringup' / 'launch' / launch_name
        text = launch_file.read_text()
        text = (text.replace(":='\"", ':=\\""')
                    .replace("\"' cam_", '"\\" cam_')
                    .replace('"\'",', '"\\"",'))
        launch_file.write_text(text)

    print('Setup done. Next: colcon build')


if __name__ == '__main__':
    main()
