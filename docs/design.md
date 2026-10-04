# Design decisions

Why the workshop is built the way it is, and what was checked. Newest decisions last.

## Platform: ROS 2 Jazzy via pixi/RoboStack, no VM

- The student's computer is likely Windows or a Mac, and we didn't want a virtual machine.
- **RoboStack** packages ROS 2 for Linux, macOS (Intel + Apple Silicon) and Windows; **pixi**
  installs it into the project folder (no admin rights, no system changes). Pixi is the official
  ROS 2 install method on Windows since ROS 2 Kilted.
- **Jazzy** rather than Humble: Humble reaches end of life in May 2027; Jazzy is supported until 2029.
- `pixi.lock` is solved for all four platforms, which proves every package exists everywhere.
  **Not yet tried on a real Windows or Mac machine.**

## Robot stack: esol-community `so101-ros-physical-ai`

Compared four community SO-101 ROS 2 stacks. Chose
[esol-community/so101-ros-physical-ai](https://github.com/esol-community/so101-ros-physical-ai)
(Apache-2.0, Jazzy, pinned commit in `scripts/setup_workspace.py`) because it has a
`hardware_type:=mock|real` switch and a real Feetech servo driver: moving to a physical arm later
changes one launch argument, not the student's code.

`setup_workspace.py` patches it:

| Change | Why |
|---|---|
| `pick_ik` → KDL IK, `position_only_ik: true` | `pick_ik` is Linux-only on RoboStack; the SO-101 has 5 joints, so "get the gripper *here*" (position only) is the right default |
| `project(... LANGUAGES NONE)` + Ninja | These packages contain no C++, so no compiler (or Visual Studio on Windows) is needed |
| Camera, LeRobot and driver packages skipped (`COLCON_IGNORE`) | Not needed for simulation; fewer dependencies |
| RViz "Loop Animation" off | The endlessly replaying planned path confused people |

## The `Arm` helper (`workshop_arm/arm.py`)

- Talks to MoveIt with plain ROS 2 actions (`/move_action`) instead of `moveit_py`, which isn't
  available on Windows.
- Beginner API: degrees, named poses, `move_to(x, y, z)`, `grab()` / `release()`.
- Blocks and bins live in MoveIt's planning scene, so they appear in RViz and are shared by
  every node. Blocks are allowed to collide (the gripper must touch them); bins are obstacles.
- `grab()` only catches a block within 2 cm of the gripper, so bad perception shows up as a miss.
- `move_to` rejects points beyond 0.44 m from the shoulder instantly, with a clear message.
- Measured accuracy: `move_to` reaches targets within ~5 mm.

## Simulation stages

`workshop.launch.py stage:=1|2|3`: arm only → bins and known blocks → random blocks + overhead
camera + detector. Lets lessons start simple and add perception later.

## Viewing and the camera: MuJoCo as a renderer

- **Why not Gazebo:** its GUI is officially unstable on macOS and experimental on Windows.
  MuJoCo installs from conda-forge on all four platforms.
- **MuJoCo only draws; no physics.** MoveIt + ros2_control mock hardware still move the arm.
  `sim_view` builds its model from `/follower/robot_description` (the same URDF as MoveIt and
  RViz), copies `/follower/joint_states` every frame, and mirrors the planning scene's blocks/bins.
- An earlier version used a separate MuJoCo Menagerie model (it had a wrist-camera mount, so the
  arms looked different); replaced by the single-URDF approach.
- **Overhead camera, not wrist camera:** one fixed pixel→table formula, sees the whole table, easy
  to debug, and on hardware it's a webcam on a stand. Wrist camera is a "Beyond" project.
- MuJoCo's physics could later replace mock hardware for real grasping ("Stage 4"), as a bridge
  to physical hardware.

## Perception

- `vision.py` is plain OpenCV (no ROS): HSV color masks → contours → size filter → pinhole model
  (camera height and focal length from `table.py`) → table coordinates. Works unchanged on webcam
  pictures; with a real webcam, a 4-corner homography would replace the pinhole math.
- Measured: detections within ~1 mm of the true block positions. In every verified stage 3 run
  (3–8 random blocks each, checked against the planning scene afterwards) all blocks ended up in
  the right bin.
- The arm can block the camera's view (and pieces of a partly covered bin rim look like blocks),
  so `vision_demo` parks the arm in a `look` pose before each picture.

## Performance (measured on an Intel integrated GPU)

| Problem | Fix | Result |
|---|---|---|
| `block_detector` at ~500% CPU | `cv2.setNumThreads(1)` | ~20% |
| `rqt_image_view` ~150% CPU per window, laggy | `sim_view` shows its own OpenCV window | one light window |
| Renders ~45 ms each | 1024 shadow map in the 3D view, no shadows in the camera, cheaper noise | camera 15 Hz, joint states ~100 Hz |
| RViz looks choppier | Not a bug: RViz's robot updates ~18 Hz (TF) / ~8 Hz (planning scene) | the simulation window is the place to *watch* |
