import decimal

from seminar4.bus_route import BusRoute


class Ticket:

    def __init__(self, route_number: BusRoute, has_luggage: bool):
        self.route_number = route_number
        self.price = 25
        self.has_luggage = has_luggage

    @property
    def price(self) -> decimal:
        if self.has_luggage:
            return self._price + 10
        return self._price

    @price.setter
    def price(self, new_price: int):
        self._price = new_price

    @property
    def route_number(self):
        return self._route_number

    @route_number.setter
    def route_number(self, number):
        self._route_number = number
