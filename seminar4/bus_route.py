import datetime
import time

from seminar4.bus_stop import BusStop


class BusRoute:
    def __init__(self, number_route: int, arrival_date: datetime, bus_stops: list):
        self.number_route = number_route
        self.arrival_date = arrival_date
        self.duration = len(bus_stops) * 5
        self.departure_date = 0
        self.arrival = None
        self.departure = None
        self.capacity = 0
        self.bus_stops = bus_stops

    @property
    def number_route(self) -> int:
        return self._number_route

    @number_route.setter
    def number_route(self, new_number: int):
        self._number_route = new_number

    @property
    def arrival_date(self) -> datetime:
        return self._arrival_date.ctime()

    @arrival_date.setter
    def arrival_date(self, new_date: datetime):
        self._arrival_date = new_date

    @property
    def departure_date(self) -> datetime:
        return (self._arrival_date + datetime.timedelta(minutes=self.duration)).ctime()

    @departure_date.setter
    def departure_date(self, new_date: datetime):
        self._departure_date = new_date

    @property
    def arrival(self) -> BusStop:
        return self.bus_stops[0]

    @arrival.setter
    def arrival(self, new_bus_stop: BusStop):
        self._arrival = new_bus_stop

    @property
    def departure(self) -> BusStop:
        return self.bus_stops[-1]

    @departure.setter
    def departure(self, new_bus_stop: str):
        self._departure = new_bus_stop

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def bus_stops(self) -> list:
        return self._bus_stops

    @bus_stops.setter
    def bus_stops(self, list_bus_stops: list):
        self._bus_stops = list_bus_stops

    def add_bus_stop(self, bus_stop: BusStop, position: int):
        self._bus_stops.insert(position, bus_stop)
