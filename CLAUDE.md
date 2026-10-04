# CLAUDE.md

Context for AI assistants (and humans) working in this repo.

## What this is

A workshop teaching a high-school student Python, ROS 2 and robot arms, ending with a simulated
SO-101 arm that finds colored blocks with a camera and sorts them into bins. The student starts
with zero Python. Windows or macOS is likely; no VM. Simulation only for now (real hardware is
deliberately on hold).

- `lessons/`: the course. One folder per lesson: `README.md`, starter files with `TODO`s,
  `solutions/`. Lessons 0–3 complete; 4–12 are outlines (pages only).
- `src/workshop_arm/`: the toolkit (Python package): `Arm` helper, simulation view, vision, demos,
  launch file. Students use it; they don't need to edit it.
- `scripts/setup_workspace.py`: clones the upstream SO-101 stack (pinned commit) into
  `src/so101-ros-physical-ai/` (gitignored) and patches it.
- `docs/design.md`: why things are the way they are, and what was verified.
- `docs/instructor_guide.md`: how to run sessions.

## Hard constraints (don't break these)

- **Must run natively on Windows, macOS (Intel + Apple Silicon) and Linux** via pixi/RoboStack
  (ROS 2 Jazzy). Before adding a dependency, check it exists for all four platforms in
  `pixi.lock` (`osx-64`, `osx-arm64`, `win-64`, `linux-64`). Known gaps: `pick_ik` (Linux only),
  `moveit_py` (no Windows), Gazebo (unstable GUI on macOS/Windows).
- **No C++ compiler needed.** Our packages are Python; upstream CMake packages are patched to
  `LANGUAGES NONE` and built with Ninja (`colcon_defaults.yaml`). Don't add C++ packages.
- **Classic ROS workflow** is what we teach: `pixi shell` → `colcon build` →
  `source install/setup.bash` → `ros2 launch` / `ros2 run`. pixi is only the installer; no
  `pixi run` task shortcuts.
- **Student-facing code is for beginners:** plain names, short functions, comments that explain
  *why*, degrees in the `Arm` API, friendly error messages.
- **One robot model:** MoveIt, RViz and the MuJoCo view all use `/follower/robot_description`.
- **Overhead camera** (not wrist camera) is the plan of record.

## Running things

```bash
cd ~/so101_workshop
pixi shell
colcon build && source install/setup.bash
ros2 launch workshop_arm workshop.launch.py stage:=1     # 1 = arm, 2 = known blocks, 3 = camera
ros2 run workshop_arm demo          # stage 2
ros2 run workshop_arm vision_demo   # stage 3
```

On the original dev machine, `~/.bashrc` sources ROS 2 Humble (for a separate drone workspace,
`~/ros2_ws`). Never mix the two: start from a clean shell first:
`env -i HOME=$HOME PATH=/usr/bin:/bin:$HOME/.pixi/bin DISPLAY=$DISPLAY TERM=$TERM bash --noprofile --norc`.
In non-interactive scripts use `eval "$(pixi shell-hook)"` instead of `pixi shell`.

Headless testing: `stage:=N rviz:=false view:=false`, and a separate `ROS_DOMAIN_ID` so tests
don't collide with anything the user has running.

## Testing changes

- Run every affected lesson solution against the simulation and check for
  `MoveIt could not do that` / `Missed!` in the output.
- For sorting changes, verify final block positions from the planning scene
  (`objects_in_scene()` in `arm.py`), not just the demo's own "Done!".
- Performance: `/camera/image_raw` should be ~15 Hz and `/follower/joint_states` ~100 Hz
  in stage 3.
- When killing test processes, don't `pkill -f` a pattern that also appears in your own shell
  command line: it kills the calling shell. Match installed paths (e.g. `install/lib/workshop_arm/`).

## Gotchas learned the hard way

- MuJoCo: call `mj_camlight` after `mj_kinematics`, or cameras/lights sit at the origin.
- `cv2.setNumThreads(1)`, or OpenCV's thread pool burns ~500% CPU on small images.
- `rqt_image_view` costs ~150% CPU per window; `sim_view` shows its own OpenCV window instead.
- Shadows dominate render time (integrated GPU): small shadow map in the 3D view, none in the
  camera picture.
- Unreachable `move_to` targets are rejected instantly by a distance check in `Arm.move_to`
  (MoveIt otherwise burns its full planning time before failing).
- Positive `shoulder_pan` turns the arm to its *right* (−y).

## Git

Repo: https://github.com/pattent/so101-arm-workshop (public, standalone; keep it separate from
the owner's other repos). `gh` on the dev machine is a snap that can't run git itself; push with
`git -c credential.helper= -c credential.helper='!gh auth git-credential' push`.
