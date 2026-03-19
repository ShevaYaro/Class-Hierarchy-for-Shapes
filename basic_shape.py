from abc import ABC, abstractmethod
import math
class BasicShape(ABC):
    def __init__(self, name=""):
        self._name = name
        self._area = 0.0

    @property
    def name(self):
        """Getter for the shape's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for the shape's name."""
        self._name = value

    @property
    def area(self):
        """Getter for the shape's area."""
        return self._area

    @area.setter
    def area(self, value):
        """Setter for the shape's area."""
        self._area = value

    @abstractmethod
    def calc_area(self):
        pass

