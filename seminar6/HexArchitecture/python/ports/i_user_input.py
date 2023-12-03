from abc import ABC, abstractmethod


class iUserInput(ABC):
    @abstractmethod
    def handleUserInput(self, userCommand):
        """ Принимает пользовательский запрос """
