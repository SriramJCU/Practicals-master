from my_guitars import Guitars

first_guitar = Guitars("Gibson L-5 CES", 1922, 16035.40)
second_guitar = Guitars("Frostman L-8 EFG", 2013, 4058.48)
third_guitar = Guitars("Spectre L-15 MSE", 1899, 50289.55)

guitar_collection = [first_guitar, second_guitar, third_guitar]

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_collection.append(Guitars(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")

print("These are my guitars:")
i = 0
for guitar in guitar_collection:
    i = guitar_collection.index(guitar)
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format((i+1), guitar.name, guitar.year, int(guitar.cost), vintage_string))
