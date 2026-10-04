# Lesson 13: MoveIt and obstacles

**Goal:** see how MoveIt plans motions that avoid hitting things. MoveIt keeps a
**planning scene**: its picture of the world, including obstacles.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1`

## Exercises (together)

1. **Plan by hand.** In RViz's MotionPlanning panel: drag the goal, click **Plan**, watch the
   preview, then **Execute**.
2. **Add obstacles.** Use `arm.add_bin(...)` (a flat box) and see it appear in RViz and in the
   simulation window. Plan a motion that has to go around it.
3. **When planning fails.** Put a target inside an obstacle. What does `move_to` return? What
   does MoveIt print?

## Challenge (on your own)

Place an obstacle between the gripper and a target, and get the arm to the target anyway.
Watch the path MoveIt picks.

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 14: Pick and place](../14_pick_and_place/)
