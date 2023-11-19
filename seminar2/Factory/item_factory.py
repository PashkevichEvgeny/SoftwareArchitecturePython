from abc import abstractmethod, ABC


class ItemFactory(ABC):
    @abstractmethod
    def create_item(self):
        pass
    