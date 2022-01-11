from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    current_taxi = None
    bill_to_date = 0
    user_choice = input(">>> ").lower()
    while user_choice != 'q':
        if user_choice == 'c':
            print("Taxis available:")
            show_all_taxis(taxis)
            chosen_taxi = get_valid_input("Chosen taxi: ")
            if chosen_taxi > (len(taxis) - 1):
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[chosen_taxi]
        elif user_choice == 'd':
            if current_taxi is not None:
                distance = get_valid_input("Drive how far: ")
                current_taxi.drive(distance)
                fare = float(current_taxi.get_fare())
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                bill_to_date += fare
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        user_choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill_to_date}")
    print("Taxis are now:")
    show_all_taxis(taxis)


def show_all_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_input(prompt):
    valid_input = False
    while not valid_input:
        try:
            user_input = int(input(prompt))
            if user_input >= 0:
                valid_input = True
                return user_input
            else:
                print("Input must be > 0")
        except ValueError:
            print("Invalid input")


if __name__ == '__main__':
    main()
