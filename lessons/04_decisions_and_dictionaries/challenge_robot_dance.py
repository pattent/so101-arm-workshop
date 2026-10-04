"""Challenge (Bronze): choreograph a 30-second robot dance!

Run (with the stage 1 simulation running):  python challenge_robot_dance.py

Ideas:
- A dictionary of dance moves (named poses).
- Functions for moves that repeat (a wave, a spin, a bow).
- A list that says the order of the moves: the "choreography".
- Change arm.speed for slow and fast parts.
- Open and close the gripper like it's clapping: arm.open_gripper(), arm.close_gripper().
- If a move fails (returns False), skip to the next one instead of stopping.
- Bonus: make it exactly long enough. `import time`, and `start = time.time()` before the
  dance; then `time.time() - start` is how many seconds have passed. Use a `while` loop to
  keep repeating your choreography until 30 seconds are up:
      while time.time() - start < 30:
"""

from workshop_arm import Arm

arm = Arm()
arm.go_to('rest')

# Your dance goes here!

arm.go_to('rest')
arm.shutdown()
