from taxi import Taxi

# 1

new_taxi = Taxi("Prius 1", 100)

# 2

new_taxi.drive(40)

# 3

print("{}, Current fare: {}".format(new_taxi, new_taxi.get_fare()))

# 4

new_taxi.start_fare()

# 5

new_taxi.drive(100)

# 6

print("{}, Current fare: {}".format(new_taxi, new_taxi.get_fare()))

