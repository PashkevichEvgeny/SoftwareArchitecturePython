# 3) Переписать код в соответствии с Interface Segregation Principle:
from abc import ABC, abstractmethod
from math import pi


class ShapeArea(ABC):
    @abstractmethod
    def area(self):
        pass


class ShapeVolume(ABC):
    @abstractmethod
    def volume(self):
        pass


class Circle(ShapeArea):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * pi * self.radius


class Cube(ShapeArea, ShapeVolume):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return self.edge ** 2 * 6

    def volume(self):
        return self.edge ** 3

# Подсказка: круг не объемная фигура и этому классу не нужен метод volume().


cube = Cube(5)
print(cube.volume(), cube.area())