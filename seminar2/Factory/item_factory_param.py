from abc import abstractmethod, ABC


class ItemFactoryParam(ABC):
    @abstractmethod
    def create_item(self, name):
        pass
    