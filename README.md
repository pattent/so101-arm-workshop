# SO-101 Robot Arm Workshop

Learn Python, ROS 2 and robot arm programming with a simulated SO-101 arm.
Runs natively on **Windows, macOS or Linux**: no virtual machine needed.

We use [pixi](https://pixi.sh) only to **install** ROS 2 Jazzy (it's the official way to install
ROS 2 on Windows). After that, everything is the standard ROS 2 workflow: `source`,
`colcon build`, `ros2 launch`, `ros2 run`.

## 1. Install pixi (one time)

**macOS / Linux** (Terminal):
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows** (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

Then close and reopen your terminal.

> **Windows:** put this folder somewhere with a short path, like `C:\so101`. Windows has
> trouble with very long file paths.

## 2. Download this workshop

```bash
pixi global install git    # only if you don't already have git
git clone https://github.com/pattent/so101-arm-workshop.git
cd so101-arm-workshop
```

## 3. Install ROS 2 and set up the workspace (one time, ~5 minutes, ~6 GB)

From inside this folder:
```bash
pixi install                        # downloads ROS 2 Jazzy, MoveIt 2, RViz, OpenCV...
pixi shell                          # turns on ROS 2 in this terminal
python scripts/setup_workspace.py   # downloads the SO-101 robot packages
colcon build                        # builds the workspace
```

## 4. Every new terminal

```bash
cd so101-arm-workshop
pixi shell                     # ROS 2 Jazzy (like `source /opt/ros/jazzy/setup.bash`)
source install/setup.bash      # our workspace   (Windows: call install\setup.bat)
```

Re-run the `source` line after every `colcon build`.

## 5. See the robot move

Terminal 1: start the simulated arm, controllers, MoveIt and RViz:
```bash
ros2 launch so101_bringup follower_moveit_demo.launch.py hardware_type:=mock
```

Terminal 2: sort a red and a blue block into matching bins:
```bash
ros2 run workshop_arm demo
```

Then try dragging the arm's marker in RViz and clicking **Plan & Execute**.

## Writing your own code

```python
from workshop_arm import Arm

arm = Arm()
arm.go_to('rest')                     # saved poses: 'rest', 'zero', 'extended'
arm.move_joints(0, -45, 90, 45, 0)    # 5 joint angles, in degrees
arm.move_to(0.25, 0.0, 0.10)          # gripper position in meters (x forward, y left, z up)
arm.open_gripper()
arm.close_gripper()
print(arm.where_am_i())               # current gripper (x, y, z)
arm.shutdown()
```

Save it as `my_first_robot.py` and run `python my_first_robot.py` (in a terminal set up
as in step 3) while the launch file is running.

## What's in here

| Path | What it is |
|---|---|
| `pixi.toml` | Everything we install (ROS 2, MoveIt, OpenCV...) |
| `colcon_defaults.yaml` | Default `colcon build` options (used automatically inside `pixi shell`) |
| `scripts/setup_workspace.py` | Downloads the SO-101 packages and adapts them for the workshop |
| `src/workshop_arm/` | The beginner-friendly `Arm` helper and the demo |
| `src/so101-ros-physical-ai/` | SO-101 robot model, controllers and MoveIt config ([upstream](https://github.com/esol-community/so101-ros-physical-ai)) |

## Notes for instructors

- Simulated vs. real arm is one launch argument: `hardware_type:=mock` today, `hardware_type:=real`
  with a real SO-101. Student code does not change.
- Upstream uses the `pick_ik` IK solver, which is Linux-only on RoboStack, so setup switches to KDL
  with position-only IK.
- `moveit_py` is not available on Windows, so `workshop_arm` talks to MoveIt using plain ROS 2 actions.
- The robot packages are patched to `LANGUAGES NONE` and built with Ninja, so no C++ compiler
  (or Visual Studio) is needed.
- If your own `~/.bashrc` sources another ROS install (e.g. Humble), start from a clean shell first:
  `env -i HOME=$HOME PATH=/usr/bin:/bin:$HOME/.pixi/bin DISPLAY=$DISPLAY TERM=$TERM bash --noprofile --norc`
