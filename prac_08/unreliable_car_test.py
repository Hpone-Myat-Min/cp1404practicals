from unreliable_car import UnreliableCar


def main():
    # Creating a new car with a name of 'Audi 100 Sedan', 90 units of fuel and 40% reliability
    car_1 = UnreliableCar('Audi 100 Sedan', 90, 0.40)

    # Test driving the car
    car_1.drive(30)

    # Print details
    print(car_1)

    # Second test drive
    car_1.drive(55)
    print(car_1)


if __name__ == '__main__':
    main()
