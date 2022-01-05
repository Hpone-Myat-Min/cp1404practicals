from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self):
        super().__init__(name='', fuel=0)
        self.fanciness = 0
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall}"

    def calculate_fare(self):
        """ Calculate the fare."""
        return super().get_fare() + SilverServiceTaxi.flagfall





