from ast import List
from abc import ABC, abstractmethod


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
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []

    def get_scene(self, id_):
        for scene in self.scenes:
            if scene.id == id_:
                return scene
        return None

    def notify_change(self, sender) -> None:
        return super().notify_change(sender)



