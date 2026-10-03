"""Solution: Exercise 3."""

import math

x = 0.25
y = 0.10

# TODO 1
distance = math.sqrt(x ** 2 + y ** 2)
print(f'The gripper is {distance:.3f} meters from the base.')

# TODO 2
print(f'math.hypot says {math.hypot(x, y):.3f} meters.')

max_reach = 0.48

# TODO 3
far_distance = math.hypot(0.40, 0.30)
print(f'(0.40, 0.30) is {far_distance:.3f} m away; the arm reaches {max_reach} m.')
# 0.5 m is more than 0.48 m, so it's just out of reach.
