
from basic_shape import BasicShape


class Rectangle(BasicShape):
    def __init__(self, l, w, n="Rectangle"):
        super().__init__(name=n)

        self._length = l
        self._width = w

        self.calc_area()

    def calc_area(self):
        """Computes the rectangle's area (length * width) and stores it."""
        self.area = self._length * self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
        self.calc_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

        self.calc_area()

