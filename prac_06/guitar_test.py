from guitar import Guitars

first_guitar = Guitars("Gibson L-5 CES", 1922, 16035.40)
second_guitar = Guitars("Frostman L-8 EFG", 2013, 4058.48)
third_guitar = Guitars("Spectre L-15 MSE", 1899, 50289.55)

print(f"{first_guitar.name} get_age() - Expected 100, Got {first_guitar.get_age()}")
print(f"{second_guitar.name} get_age() - Expected 9, Got {second_guitar.get_age()}")
print(f"{first_guitar.name} is_vintage() - Expected True, Got {first_guitar.is_vintage()}")
print(f"{second_guitar.name} is_vintage() - Expected False, Got {second_guitar.is_vintage()}")