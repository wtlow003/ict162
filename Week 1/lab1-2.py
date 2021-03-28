class Rectangle:
    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    '''Getter, Setter methods for length, width'''
    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, new_length):
        self._length = new_length

    @width.setter
    def width(self, new_width):
        self._width = new_width

    def get_area(self):
        '''Returns area of the rectangle'''
        return self._length * self._width

    def get_perimeter(self):
        '''Returns the perimeter of the rectangle'''
        return (2 * self._length) + (2 * self._width)

    def increase_size(self, length_increase, width_increase):
        '''Increase the length and width of the rectangle by given amounts'''
        self._length += length_increase
        self._width += width_increase

    def is_bigger(self, r):
        '''Return boolean, True if current area is igger than area of rectangle r'''
        return self.get_area() > r.get_area()

    def __str__(self):
        return f"{self._length} {self._width} {self.get_area()} {self.get_perimeter()}"


if __name__ == '__main__':
    r1 = Rectangle(20.0, 10.0)
    r2 = Rectangle(15.0, 5.0)
    print(r1, r2, sep='\n')
    # getting the area
    print(r1.get_area(), r2.get_area())
    # getting the perimeter
    print(r1.get_perimeter(), r2.get_perimeter())
    print(r1.is_bigger(r2))
    # increase the size of r2
    r2.increase_size(10.0, 10.0)
    print(r2.get_area(), r2.get_perimeter())
    print(r1.is_bigger(r2))
