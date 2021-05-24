# LAB4 (Exception Handling)


class EmptyBoxException(Exception):
    """Raise exception for violation in Box classes"""


class Box:

    _max_items = 10

    def __init__(self, number_of_items):
        if number_of_items > type(self)._max_items:
            raise EmptyBoxException("Exceed the max number of items the box can hold.")
        else:
            self._number_of_items = number_of_items

    @property
    def number_of_items(self):
        return self._number_of_items

    def remove(self, items):
        if self._number_of_items - items < 0:
            raise EmptyBoxException("Removal results in negative number of items.")
        else:
            self._number_of_items -= items

    def add(self, items):
        if self._number_of_items + items > type(self)._max_items:
            raise EmptyBoxException("Addition results in more than max items allowed.")
        else:
            self._number_of_items += items


class Demo:

    def __init__(self, box):
        self._box = box

    def add(self, items):
        try:
            self._box.add(items)
        except EmptyBoxException as e:
            print(e)

    def remove(self, items):
        try:
            self._box.remove(items)
        except EmptyBoxException as e:
            print(e)


if __name__ == '__main__':
    # test if we can add more than the max items
    # b = Box(15)
    # print(b)  >> exceed, hence cannot
    b = Box(10)
    d = Demo(b)
    # current box has == 10 items
    print(d._box.number_of_items)
    # not allowed as the number exceed 10
    d.add(5)
    # remove - 11 not allowed as negative
    d.remove(11)
    # remove 5
    d.remove(5)
    print(d._box.number_of_items)
    # add back 5
    d.add(5)
    print(d._box.number_of_items)