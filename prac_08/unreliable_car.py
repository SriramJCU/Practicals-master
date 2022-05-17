import random
from car import Car

class UnreliableCar(Car):
    """Specialised version of car that is unreliable"""

    def __init__(self, name, fuel, reliability):
        """Initial variables of class object"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, reliability = {}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        random_float = random.uniform(1, 100)
        if self.reliability > random_float:
            super().drive(distance)
        return distance



