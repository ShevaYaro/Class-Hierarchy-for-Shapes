from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, s, n="Square"):

        super().__init__(s, s, n)

        self._side = s

        self.name = n

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

        self.length = value
        self.width = value

