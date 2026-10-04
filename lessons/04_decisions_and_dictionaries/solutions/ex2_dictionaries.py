"""Solution: Exercise 2."""

bins = {
    'red': (0.12, 0.22),
    'green': (0.24, 0.20),
    'blue': (0.34, 0.12),
}

print('The red bin is at', bins['red'])
print('There are', len(bins), 'bins')

# TODO 1
print('The blue bin is at', bins['blue'])
x, y = bins['blue']
print('Its x is', x)

# TODO 2: bins['purple'] fails with  KeyError: 'purple'
if 'purple' in bins:
    print('The purple bin is at', bins['purple'])
else:
    print('There is no purple bin')

bins['yellow'] = (0.20, 0.25)
print('Now the bins are:', bins)

# TODO 3
bins['green'] = (0.26, 0.18)
print('After moving green:', bins)

for color, position in bins.items():
    print(f'The {color} bin is at {position}')

# TODO 4
seen = ['red', 'blue', 'red', 'green', 'red', 'blue']
counts = {}
for color in seen:
    if color in counts:
        counts[color] = counts[color] + 1
    else:
        counts[color] = 1
print(counts)            # {'red': 3, 'blue': 2, 'green': 1}

# TODO 5
poses = {
    'up': [0, -90, 0, 0, 0],
    'bow': [0, -20, 20, 70, 0],
}
print(poses['up'])
print(poses['up'][1])    # -90
