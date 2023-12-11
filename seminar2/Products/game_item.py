from abc import abstractmethod, ABC


class GameItem(ABC):
    @abstractmethod
    def look(self):
        pass
