from datetime import datetime
from random import randint, sample

from seminar4.bus_route import BusRoute
from seminar4.bus_stop import BusStop
from seminar4.person import Person
from seminar4.ticket import Ticket

if __name__ == '__main__':
    list_routes = []
    bus_stops = []
    stops_name = ['Ленина', 'Мира', 'Лермотнова', 'Рынок', 'Больница', 'Пушкина', 'Музей', 'Кинотеатр Заря']
    for name in stops_name:
        x, y = randint(0, 100) + randint(0, 10 ** 6) * 0.1 ** 6, randint(0, 100) + randint(0, 180 ** 6) * 0.1 ** 6
        x, y = x if randint(0, 2) else -x, y if randint(0, 2) else -y
        bus_stops.append(BusStop(name, x, y))

    for i in range(1, 6):
        list_routes.append(BusRoute(i, datetime.now(),
                           sample(bus_stops, 5)))

    for i in list_routes:
        print(i.number_route, i.arrival.name, '-', i.departure.name)

    chosen_route = list_routes[int(input('Выберите маршрут: ')) - 1]
    luggage = bool(input('Для провоза багажа нажмите 1 иначе 0: '))
    login, password = input('Введите логин, пароль: ').split()
    card = int(input('Введите номер карты: '))
    passenger = Person(login, card, password)
    if input('Нажмите ДА для покупки билета: ') == 'ДА':
        ticket = Ticket(chosen_route, luggage)
        passenger.buy_ticket(chosen_route, ticket)
    passenger.show_ticket()


