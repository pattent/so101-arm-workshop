"""Exercise 2: functions.

A function gives a name to a few steps, so you can reuse them.

Run (with the stage 1 simulation running):  python ex2_wave.py
"""

from workshop_arm import Arm


def arm_up(arm):
    """Point the arm straight up."""
    arm.move_joints(0, -90, 0, 0, 0)


# TODO 1: Finish this function. It should tip the wrist one way (wrist_flex = 40),
#         then the other way (wrist_flex = -40), `times` times.
#         Use a for loop with range(times).
def wave(arm, times):
    arm_up(arm)
    # your loop goes here


arm = Arm()
arm.go_to('rest')

wave(arm, 3)

# TODO 2: Add a `speed` setting: arm.speed can be from 0.1 (slow) to 1.0 (fast).
#         Wave 2 times slowly, then 2 times fast.

# TODO 3: Write a function nod(arm, times) that nods "yes" with the shoulder_lift
#         joint, and call it.

arm.go_to('rest')
arm.shutdown()
