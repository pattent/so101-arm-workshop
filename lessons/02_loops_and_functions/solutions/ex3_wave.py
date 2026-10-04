"""Solution: Exercise 3."""

from workshop_arm import Arm


def arm_up(arm):
    """Point the arm straight up."""
    arm.move_joints(0, -90, 0, 0, 0)


# TODO 1
def wave(arm, times):
    arm_up(arm)
    for i in range(times):
        arm.move_joints(0, -90, 0, 40, 0)
        arm.move_joints(0, -90, 0, -40, 0)


# TODO 3
def nod(arm, times):
    arm_up(arm)
    for i in range(times):
        arm.move_joints(0, -60, 0, 0, 0)
        arm.move_joints(0, -90, 0, 0, 0)


arm = Arm()
arm.go_to('rest')

wave(arm, 3)

# TODO 2
arm.speed = 0.2
wave(arm, 2)
arm.speed = 1.0
wave(arm, 2)
arm.speed = 0.5

nod(arm, 2)

arm.go_to('rest')
arm.shutdown()
