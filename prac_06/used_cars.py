"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Land Rover", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # 1. Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("Splendid Limo", 100)

    # Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)

    # 3. Print the amount of fuel in the car.
    print(f"Amount of fuel: {limo.fuel} units")

    # 4. Attempt to drive the car 115 km using the drive method.
    limo.drive(115)

    # 5. Print the car's odometer reading.
    print(f"Odometer reading: {limo.odometer}")

    # 8. print your car object/s to make sure that the __str__ method is working as expected.
    print(limo)


main()
