from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Main Program"""
    taxis = [
        Taxi("Altis", 100),
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]

    total_trip_cost = 0
    print("Let's drive!")
    current_taxi = None

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ")
        if choice.lower() == "q":
            print("Total trip cost: ${:.2f}".format(total_trip_cost))
            print("Taxis are now:")
            list_taxis(taxis)
            break

        elif choice.lower() == "c":
            print("Taxis available:")
            list_taxis(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice!")
            print("Bill to date: ${:.2f}".format(total_trip_cost))

        elif choice.lower() == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
                total_trip_cost += fare
                print("Bill to date: ${:.2f}".format(total_trip_cost))
        else:
            print("Invalid option")


def list_taxis(taxis):
    """List the taxis available and their details"""
    for taxi in taxis:
        print("{} - {}".format(taxis.index(taxi), taxi))


main()
