from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass