class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, new_x):
        self._x = x

    @y.setter
    def y(self, new_y):
        self._y = y

    def move(self, dx, dy):
        '''Method to move x and y by dx, dy'''
        self._x += dx
        self._y += dy

    def distance_to(self, a_point):
        '''Method to return the distance to another point (x1, y1)'''
        return ((self._x - a_point.x) ** 2 + (self._y - a_point.y) ** 2) ** 0.5

    def quadrant(self):
        if self._x == 0 or self._y == 0:
            return 0
        elif self._x > 0 and self._y > 0:
            return 1
        elif self._x < 0 and self._y < 0:
            return 3
        elif self._x > 0 and self._y < 0:
            return 2
        else:
            return 4

    def __str__(self):
        return f"({self._x}, {self._y})"


if __name__ == '__main__':
    # create a point object at (5, 1)
    p1 = Point(5, 1)
    # print coordinate of p1
    print(p1)
    # move p1 by delta (5, -5)
    p1.move(5, -5)
    p2 = Point(10, -10)
    print(p1.distance_to(p2))
    print(p1.quadrant(), p2.quadrant())
