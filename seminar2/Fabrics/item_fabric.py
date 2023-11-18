from abc import abstractmethod, ABC


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass
    