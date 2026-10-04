"""Solution: Exercise 1."""

import random
import time


def shout(text):
    print(text.upper() + '!')


say_it = shout
say_it('hello')


# TODO 1
def do_twice(action, text):
    action(text)
    action(text)


do_twice(shout, 'robots')
do_twice(print, 'robots')


class DistanceSensor:
    """Measures how far away the nearest object is (in meters), a few times a second."""

    def __init__(self):
        self.callbacks = []

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def run(self, readings):
        for _ in range(readings):
            distance = round(random.uniform(0.05, 0.50), 2)
            for callback in self.callbacks:
                callback(distance)
            time.sleep(0.2)


def on_reading(distance):
    print(f'Something is {distance} m away')


sensor = DistanceSensor()
sensor.subscribe(on_reading)
sensor.run(5)


# TODO 2
def too_close(distance):
    if distance < 0.10:
        print('  WARNING: too close!')


sensor.subscribe(too_close)
sensor.run(5)


# TODO 3
class ClosestTracker:
    def __init__(self):
        self.closest = None

    def on_reading(self, distance):
        if self.closest is None or distance < self.closest:
            self.closest = distance


tracker = ClosestTracker()
sensor.subscribe(tracker.on_reading)
sensor.run(10)
print('The closest reading was', tracker.closest, 'm')

# Think about it: `sensor.subscribe(on_reading)` does the same job as create_subscription.
