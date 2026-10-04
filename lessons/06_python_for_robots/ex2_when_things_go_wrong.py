"""Exercise 2: when things go wrong.

Robot programs meet bad data all the time: a typo from the keyboard, a glitchy sensor, a
target the arm can't reach. Python tells you about a problem by "raising an error". If
nobody catches it, the program stops and prints a traceback.

Run:  python ex2_when_things_go_wrong.py   (no robot needed)
"""

# Part 1: read a traceback.
# TODO 1: Remove the # in front of the next line and run the program. Read the error
#         from the BOTTOM up:
#           - the last line says WHAT went wrong (the kind of error, and a message)
#           - the lines above say WHERE (file name and line number)
#         Then put the # back.
# print(float('twenty'))


# Part 2: catch an error with try / except.
def read_height(text):
    """Turn text like '0.12' into a number. Return None if it isn't a number."""
    try:
        return float(text)        # try this...
    except ValueError:
        print(f'  "{text}" is not a number, skipping it')
        return None               # ...and do this instead if it raises a ValueError


for text in ['0.12', '0.30', 'oops', '0.05']:
    print(text, '->', read_height(text))

# TODO 2: Ask for a height with input(), and keep asking until the person types a real
#         number. (Hint: a while loop, and read_height returns None for bad input.)


# Part 3: raise your own errors, with a helpful message.
ALLOWED_COLORS = ['red', 'green', 'blue']


def check_color(color):
    if color not in ALLOWED_COLORS:
        raise ValueError(f'Unknown color {color!r}. Try one of: {ALLOWED_COLORS}')
    return color


print(check_color('red'))

# TODO 3: Call check_color('purple') inside a try / except that catches the ValueError
#         and prints the message. (Hint: `except ValueError as error:` then print(error).)

# TODO 4: Make a list of colors: ['red', 'purple', 'blue', 'pink', 'green'].
#         Loop over it and print only the good colors, skipping the bad ones with
#         try / except. The program must not crash.

# Think about it: when should a robot program catch an error and carry on, and when is it
# better to stop? (Would you rather a robot skip a bad camera reading, or keep moving after
# its motors stop responding?)
