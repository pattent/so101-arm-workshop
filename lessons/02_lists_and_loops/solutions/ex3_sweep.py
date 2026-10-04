"""Solution: Exercise 3."""

from workshop_arm import Arm

for i in range(3):
    print('Counting:', i)
print('The sweep angles:', list(range(-60, 61, 30)))

arm = Arm()
arm.go_to('rest')

for pan in range(-60, 61, 30):
    print('shoulder_pan =', pan)
    arm.move_joints(pan, -45, 45, 45, 0)

# TODO 1
for pan in range(60, -61, -30):
    arm.move_joints(pan, -45, 45, 45, 0)

# TODO 2 and 3
moves = 0
positions = []
for pan in range(-60, 61, 15):
    arm.move_joints(pan, -45, 45, 45, 0)
    moves = moves + 1
    positions.append(arm.where_am_i())
print('That took', moves, 'moves')       # 9
print('Positions:', positions)
print('First:', positions[0], ' last:', positions[-1])

arm.go_to('rest')
arm.shutdown()
