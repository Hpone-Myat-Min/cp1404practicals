from taxi import Taxi


def main():
    # 1. Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    taxi1 = Taxi("Prius 1", 100, 1.23)

    # 2. Drive the taxi 40 km
    taxi1.drive(40)

    # 3. Print the taxi's details and the current fare
    print(taxi1)
    print(f"Current fare: ${taxi1.get_fare():.2f}")

    # 4. Restart the meter (start a new fare) and then drive the car 100 km
    taxi1.start_fare()
    taxi1.drive(100)

    # 5. Print the details and the current fare
    print(taxi1)
    print(f"Current fare: ${taxi1.get_fare():.2f}")


if __name__ == '__main__':
    main()
