from abc import abstractmethod, ABC


class GameItem(ABC):
    @abstractmethod
    def open(self):
        pass
