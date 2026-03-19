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

class Circle(BasicShape):
    def __init__(self, x, y, r, n="Circle"):

        super().__init__(name=n)

        self._x_center = x
        self._y_center = y
        self._radius = r

        self.area = math.pi * (self._radius ** 2)
#  Properties for x_center and y_center 
    @property
    def x_center(self):
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        self._x_center = value

    @property
    def y_center(self):
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        self._y_center = value

    #  Property for radius 
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

        self.calc_area()