"""Exercise 1: your first class, from scratch.

In Lesson 1 you used the Rover class and gave it a battery. Here it is again, as a reminder
of how a class is built. This time you'll write a whole class of your own.

Run:  python ex1_my_first_class.py   (no robot needed)
"""


# A rover that drives along a straight line.
class Rover:

    # __init__ runs once, when a new rover is made. `self` means "this rover".
    # Its attributes (the variables stored on self) are what it remembers.
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.battery = 100

    # Each method is something the rover can do. It gets `self` first, so it can use the
    # rover's own attributes.
    def report(self, message):
        print(f'{self.name}: {message}')

    def drive(self, meters):
        self.position = self.position + meters
        self.battery = self.battery - 5 * abs(meters)    # abs: driving backward costs too
        print(f'{self.name} drives {meters} m, to {self.position} m.')


curiosity = Rover('Curiosity')
curiosity.report('Systems online.')
curiosity.drive(3)
curiosity.drive(2)
print('Curiosity is at', curiosity.position, 'm with', curiosity.battery, '% battery')

# TODO 1: Add a method return_to_base(self) that drives the rover back to 0.
#         (Hint: it can call self.drive(...) with the right number of meters.)
#         Test it on curiosity, then print its position and battery.

# TODO 2: Make drive refuse to go if the trip would use more battery than is left: report
#         "Not enough battery" and don't move. (`if` from Lesson 4.) Test it with a long drive.

# TODO 3: Your turn: write your own class from scratch, for anything you like. Some ideas:
#         a Drone (name, height, battery: take_off, land), a BankAccount (owner, balance:
#         deposit, withdraw), or a Playlist (name, list of songs: add, play).
#         Give it an __init__ that stores at least two attributes, and at least two methods.
#         Then make two objects from it, and call their methods.
