"""Solution: Exercise 1."""

from workshop_arm import Arm


# TODO 2
def try_points(arm, points):
    for x, y, z in points:
        if arm.move_to(x, y, z):
            print(f'({x}, {y}, {z}) worked!')
            return True
        print(f'({x}, {y}, {z}) did not work, trying the next one...')
    print('None of the points worked.')
    return False


arm = Arm()
arm.go_to('rest')

ok = arm.move_to(0.25, 0.0, 0.15)
print('Did the first move work?', ok)

if ok:
    print('Yes! The gripper is at', arm.where_am_i())
else:
    print('No, that point was not reachable.')

far_away = (0.60, 0.0, 0.10)

# TODO 1
x, y, z = far_away
if not arm.move_to(x, y, z):
    print('Too far! Going to the backup point.')
    arm.move_to(0.30, 0.0, 0.10)

try_points(arm, [(0.70, 0.0, 0.1), (0.50, 0.2, 0.1), (0.25, 0.1, 0.12)])

arm.go_to('rest')
arm.shutdown()
