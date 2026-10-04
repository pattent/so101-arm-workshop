"""Exercise 2: dictionaries, looking things up by name (no robot needed).

A list finds things by their position: joints[0]. A dictionary finds things by a NAME
(its "key"), like the contacts on your phone: look up a name, get a number.

Run:  python ex2_dictionaries.py
"""

# Where each colored bin is on the table: color -> (x, y). Keys go before the colon,
# values after. (This is the real table: see BINS in src/workshop_arm/workshop_arm/table.py.)
bins = {
    'red': (0.12, 0.22),
    'green': (0.24, 0.20),
    'blue': (0.34, 0.12),
}

print('The red bin is at', bins['red'])     # look up a value by its key
print('There are', len(bins), 'bins')

# TODO 1: Print where the blue bin is. Then unpack it into x and y, and print just its x.

# TODO 2: Try print(bins['purple']). Read the last line of the error.
#         Then use `in` to check first (it gives back True or False):
#             if 'purple' in bins:
#                 ...
#             else:
#                 print('There is no purple bin')

# Dictionaries can change: add a new key, or give an old key a new value.
bins['yellow'] = (0.20, 0.25)
print('Now the bins are:', bins)

# TODO 3: The green bin got moved to (0.26, 0.18). Update it, and print the dictionary.


# Loop over a dictionary with .items(), which gives you each key AND its value.
for color, position in bins.items():
    print(f'The {color} bin is at {position}')

# TODO 4: Counting with a dictionary. The camera saw these blocks:
seen = ['red', 'blue', 'red', 'green', 'red', 'blue']
#         Make an empty dictionary counts = {}. Loop over seen: if the color is already in
#         counts, add 1 to it; if not, set it to 1. Print counts at the end.
#         It should be {'red': 3, 'blue': 2, 'green': 1}.

# TODO 5: Values can be anything, even lists. Make a dictionary called poses with two
#         names (like 'up' and 'bow'), each mapping to a list of five joint angles.
#         Print the angles for 'up', then just its second angle.
#         You'll use a dictionary like this in the next exercise to move the robot.
