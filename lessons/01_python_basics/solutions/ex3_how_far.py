"""Solution: Exercise 3."""

import math

x = 0.25
y = 0.10

# TODO 1
distance = math.sqrt(x ** 2 + y ** 2)
print(f'The gripper is {distance:.3f} meters from the base.')


# TODO 2
def distance_from_base(x, y):
    return math.sqrt(x ** 2 + y ** 2)


print(distance_from_base(0.25, 0.10))     # about 0.269
print(distance_from_base(0.30, -0.10))    # about 0.316


# TODO 3
def can_reach(x, y):
    return distance_from_base(x, y) < 0.48


print(can_reach(0.25, 0.10))              # True
print(can_reach(0.40, 0.30))              # False: it's 0.5 m away


# TODO 4
def shout_distance(x, y):
    print('The distance is', distance_from_base(x, y))


result = shout_distance(0.25, 0.10)
print('It gave back:', result)
# It gave back None ("nothing"): the function printed the distance, but had no `return`,
# so there was no answer to save in result.
