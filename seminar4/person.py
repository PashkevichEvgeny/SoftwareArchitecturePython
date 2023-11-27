import datetime
from hashlib import pbkdf2_hmac

from seminar4.bus_route import BusRoute
from seminar4.bus_stop import BusStop
from seminar4.ticket import Ticket


class Person:
    _id = 0

    def __init__(self, login: str, card_number: int, password: str):
        Person._id += 1
        self._id = Person._id
        self.card_number = card_number
        self.hash_pass = pbkdf2_hmac('sha256', password.encode(), login.encode(), 100, 15)
        self.login = login
        self.my_ticket = None

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        if len(new_login):
            self._login = new_login
        else:
            raise ValueError('Name is empty!')

    def buy_ticket(self, route: BusRoute, ticket: Ticket):
        self.my_ticket = ticket
        print(f'Билет на маршрут {route.number_route} {route.arrival.name} {route.departure.name} '
              f'куплен за {ticket.price}')

    def show_ticket(self):
        if self.my_ticket is None:
            print("Билета нет")
        else:
            print(f'Билет на маршрут {self.my_ticket.route_number.number_route} '
                  f'Время отправления {self.my_ticket.route_number.arrival_date}')

    @property
    def id(self):
        return self._id


