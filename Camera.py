class Camera(object):
    def __init__(self, starting_position=(0, 0)):
        self.x, self.y = starting_position

    def move_absolute(self, new_position):
        self.x, self.y = new_position

    def move(self, distance):
        self.move_absolute((self.x + distance[0], self.y + distance[1]))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
