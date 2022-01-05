from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name='', fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        distance = random.randint(0, 100)
        if distance < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
