from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name='', fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.distance_driven = 0

    def __str__(self):
        return f"{super().__str__()}, distance driven: {self.distance_driven}"

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability * 100:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        self.distance_driven = distance_driven
        return distance_driven
