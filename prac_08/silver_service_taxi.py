from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Special version of a Taxi that is Fancy"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Inintial variables of the class object"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare based on the distance travelled"""
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        """String representation of the class object"""
        return "{} plus flagfall of {}".format(super().__str__(), SilverServiceTaxi.flagfall)

