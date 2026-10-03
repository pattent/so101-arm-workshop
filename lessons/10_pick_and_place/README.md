# Lesson 10: Pick and place → 🥈 Silver

**Goal:** sort blocks whose positions you already know. This is the **Silver** tier.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=2`
(three bins, and three blocks at the spots listed in `KNOWN_BLOCKS` in
[`table.py`](../../src/workshop_arm/workshop_arm/table.py)).

## Exercises (together)

1. **Pick one block by hand.** Move above it, go down, `arm.grab()`, come back up. What does
   `grab()` return if you're 3 cm off?
2. **Functions for the steps.** Write `pick(arm, x, y)` and `place(arm, x, y)`. Why go up to a
   "safe height" between moves?
3. **Read the example.** Compare your code with
   [`demo.py`](../../src/workshop_arm/workshop_arm/demo.py) and run it:
   `ros2 run workshop_arm demo`.

## Challenge (on your own): 🥈 Silver

Write your own program that sorts all three blocks into the bins of the same color, using the
positions from `table.py`. Bonus: if a grab misses, try again a little lower.

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 11: Computer vision](../11_computer_vision/)
