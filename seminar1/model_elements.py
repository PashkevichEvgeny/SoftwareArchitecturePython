from service import Point3D
from typing import TypeVar, Generic

T = TypeVar('T')


class PolygonalModel:
    def __init__(self, textures):
        self.textures = [textures]
        self.polygons = [Polygon()]


class Flash:
    def __init__(self):
        self.location = None
        self.angle = None
        self.color = None
        self.power = 0

    def rotate(self, angle):
        pass

    def move(self, point):
        pass


class Texture:
    pass


class Polygon:
    def __init__(self):
        points = [Point3D()]


class Scene(Generic[T]):
    id = 0

    def __init__(self, models, flashes, cameras):
        self.id += 1
        self.models = []
        self.flashes = []
        self.cameras = []
        if len(models):
            self.models.append(models)
        else:
            raise Exception()
        self.flashes.append(flashes)
        if len(cameras):
            self.cameras.append(cameras)
        else:
            raise Exception()

    def method1(self, type_: T) -> T:
        pass

    def method2(self, type1: T, type2: T) -> T:
        pass


class Camera:
    def __init__(self):
        self.location = None
        self.angle = None

    def rotate(self, angle) -> None:
        pass

    def move(self, point) -> None:
        pass
