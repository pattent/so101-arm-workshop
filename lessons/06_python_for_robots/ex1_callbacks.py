"""Exercise 1: callbacks.

A callback is a function you hand to someone else, for THEM to call later, whenever
something happens. Robots are full of "whenever" moments: whenever a new camera picture
arrives, whenever a joint moves, whenever a button is pressed. ROS 2 uses callbacks for all
of them.

Run:  python ex1_callbacks.py   (no robot needed)
"""

import random
import time


# Part 1: a function is a value, just like a number or a list.
def shout(text):
    print(text.upper() + '!')


say_it = shout          # NO parentheses: we're not calling shout, we're passing it around
say_it('hello')         # now we call it, through its new name

# TODO 1: Write a function do_twice(action, text) that calls action(text) two times.
#         Test it with do_twice(shout, 'robots'), then with do_twice(print, 'robots').


# Part 2: a simulated distance sensor. You don't need to change this class; just read it.
class DistanceSensor:
    """Measures how far away the nearest object is (in meters), a few times a second."""

    def __init__(self):
        self.callbacks = []

    def subscribe(self, callback):
        """Remember a function to call with every new reading."""
        self.callbacks.append(callback)

    def run(self, readings):
        """Take `readings` measurements, and hand each one to every subscriber."""
        for _ in range(readings):
            distance = round(random.uniform(0.05, 0.50), 2)
            for callback in self.callbacks:
                callback(distance)
            time.sleep(0.2)


# Our callback. We never call it ourselves: the sensor does.
def on_reading(distance):
    print(f'Something is {distance} m away')


sensor = DistanceSensor()
sensor.subscribe(on_reading)    # "call on_reading whenever you have a reading"
sensor.run(5)

# TODO 2: Write a second callback, too_close(distance), that prints a WARNING only when
#         the distance is less than 0.10 m. Subscribe it too, and run the sensor again.
#         Both callbacks now get every reading.

# TODO 3: Callbacks can also be methods of an object, which lets them remember things
#         between calls. Finish this class so it keeps the closest distance seen so far,
#         then subscribe tracker.on_reading and run the sensor 10 times.


class ClosestTracker:
    def __init__(self):
        self.closest = None

    def on_reading(self, distance):
        pass   # TODO 3: if closest is None or distance is smaller, save it in self.closest


tracker = ClosestTracker()
# TODO 3: subscribe tracker.on_reading (no parentheses!), run, then print tracker.closest

# Think about it: in ROS, `self.create_subscription(..., self.on_joints, 10)` hands ROS your
# method on_joints. Which line above does the same job?
