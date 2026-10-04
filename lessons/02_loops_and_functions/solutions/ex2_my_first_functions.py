"""Solution: Exercise 2."""

import math


def say_hello(name):
    print(f'Hello, {name}! I am the SO-101.')


say_hello('Alex')
say_hello('Sam')


def to_radians(degrees):
    return degrees * math.pi / 180


answer = to_radians(90)
print('90 degrees is', answer, 'radians')
print('45 degrees is', to_radians(45), 'radians')


# TODO 1
def to_degrees(radians):
    return radians * 180 / math.pi


print(f'1.2 radians is {to_degrees(1.2):.2f} degrees')


# TODO 2
def distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)


print(f'(0.25, 0.10) is {distance(0.25, 0.10):.3f} m away')

# TODO 3
points = [(0.25, 0.10), (0.30, -0.10), (0.40, 0.30)]
for x, y in points:
    print(f'({x}, {y}) is {distance(x, y):.3f} m away')

# TODO 4: say_hello prints, but has no `return`, so it gives back None ("nothing").
result = say_hello('Robot')
print('say_hello gave back:', result)
