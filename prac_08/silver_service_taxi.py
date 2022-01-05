from taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.50

    def __init__(self, name='', fuel=0, fanciness=0):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
