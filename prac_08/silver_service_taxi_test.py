from silver_service_taxi import SilverServiceTaxi


def main():
    taxi_1 = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi_1)

    taxi_2 = SilverServiceTaxi("Harrier", 200, 2)
    taxi_2.drive(18)

    print(f"Fare for an 18 km trip with fanciness of 2: ${taxi_2.get_fare():.2f}")


if __name__ == '__main__':
    main()
