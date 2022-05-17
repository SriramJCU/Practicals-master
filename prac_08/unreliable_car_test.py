from random import uniform
from unreliable_car import UnreliableCar


reliability = uniform(0, 100)
car = UnreliableCar("Nightshark", 100, reliability)

# Test drive

car.drive(50)
print(car)