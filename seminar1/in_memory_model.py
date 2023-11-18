from ast import List
from abc import ABC, abstractmethod

from model_elements import PolygonalModel, Flash, Scene, Camera, Texture


class IModelChangeObserver(ABC):
    @abstractmethod
    def apply_update_model(self) -> None:
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender) -> None:
        pass


class ModelStore(IModelChanger, ABC):
    def __init__(self, change_observers: List(IModelChangeObserver)):
        self.__change_observers = []
        self.__change_observers.append(change_observers)
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []
        self.models.append(PolygonalModel(Texture()))
        self.flashes.append(Flash())
        self.cameras.append(Camera())
        self.scenes.append(Scene(self.models, self.flashes, self.cameras))

    def get_scene(self, id_):
        for scene in self.scenes:
            if scene.id == id_:
                return scene
        return None

    def notify_change(self, sender) -> None:
        return super().notify_change(sender)
