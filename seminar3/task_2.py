# 2) Переписать код SpeedCalculation в соответствии с Open-Closed Principle:
from abc import ABC, abstractmethod


class SpeedCalculation(ABC):
    @abstractmethod
    def calculate_allowed_speed(self):
        pass


class Vehicle:
    def __init__(self, max_speed, type_):
        self.max_speed = max_speed
        self.type = type_
        self.coefficient = 0

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type


class Car(Vehicle, SpeedCalculation):
    def __init__(self, max_speed, type_):
        super().__init__(max_speed, type_)
        self.coefficient = 0.8

    def calculate_allowed_speed(self):
        return self.get_max_speed() * self.coefficient


class Bus(Vehicle, SpeedCalculation):

    def __init__(self, max_speed, type_):
        super().__init__(max_speed, type_)
        self.coefficient = 0.6

    def calculate_allowed_speed(self):
        return self.get_max_speed() * self.coefficient

# Подсказка: создайте два дополнительных класса Car и Bus(наследников Vehicle), напишите метод calculateAllowedSpeed().
# Использование этого метода позволит сделать класс SpeedCalculation соответствующим OCP
