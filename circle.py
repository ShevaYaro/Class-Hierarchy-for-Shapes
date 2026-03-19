import math
from basic_shape import BasicShape

class Circle(BasicShape):
    def __init__(self, x, y, r, n="Circle"):

        super().__init__(name=n)

        self._x_center = x
        self._y_center = y
        self._radius = r

        self.calc_area()

    def calc_area(self):
        """Computes the circle's area (pi * r^2) and stores it."""
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

