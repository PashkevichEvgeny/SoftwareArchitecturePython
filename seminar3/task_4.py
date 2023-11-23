# 4) Переписать код в соответствии с Liskov Substitution Principle:
from abc import ABC, abstractmethod


class Area(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Area):
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Area):
    def __init__(self):
        self.side = 0

    def set_side(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
