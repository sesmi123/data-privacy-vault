from abc import ABC, abstractmethod

class AbstractDBConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass
    