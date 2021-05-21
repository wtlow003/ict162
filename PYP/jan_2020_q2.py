# JAN 2020 Q2
# Time for completion: 25 mins
from datetime import datetime
from jan_2020_q1 import Module


class Staff:
    _next_staff_id = 1

    def __init__(self, name):
        self._staff_int = type(self)._next_staff_id
        self._name = name
        # initialize with empty module list
        self._modules = []
        # auto increment for staff id
        type(self)._next_staff_id += 1

    def number_of_modules(self):
        return len(self._modules)

    def search_module(self, code):
        for module in self._modules:
            if code == module.code:
                return module
        return None

    def remove_module(self, code):
        for module in self._modules:
            if code == module.code:
                self._modules.remove(module)
                return True
        return False


class PartTimeStaff(Staff):

    def __init__(self, name, date_join):
        super().__init__(name)
        self._date_join = date_join

    def remove_module(self, code):
        # number of modules left after removing must not be less
        # than the minimum based on (datetime.now - _date_join)
        minimum = datetime.now().year - self._date_join.year
        if (len(self._modules) - 1) > minimum:
            for module in self._modules:
                if code == module.code:
                    self._modules.remove(module)
        return False


if __name__ == '__main__':
    p = PartTimeStaff('John', datetime.strptime('2020-06-01', '%Y-%m-%d'))
    # checking if we can remove 'B231'
    if not p.remove_module('B231'):
        print('Unsuccessful remove.')
    print(p._name, p._staff_int)