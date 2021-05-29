# JAN 2020 Q3
from abc import ABC, abstractmethod

class StaffManagementException(Exception):
    """User defined exception for business rule violation in Staff Management.
    """


class Staff(ABC):
    def __init__(self, staff_id, name, salary):
        self._staff_id = staff_id
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise StaffManagementException("Salary cannot be zero or negative.")
        else:
            self._salary = new_salary

    @property
    def name(self):
        return self._name

    @abstractmethod
    def allowance(self):
        pass

    def gross_salary(self):
        return self.allowance() + self._salary


class SupportStaff(Staff):

    _base_allowance = 200

    def allowance(self):
        return round(type(self)._base_allowance + 0.02 * self._salary, 0)


class Manager(Staff):

    def allowance(self):
        return 1500


class Department:

    def __init__(self, budget, name, manager):
        self._budget = budget
        if manager.gross_salary() > budget:
            raise StaffManagementException("Manager's salary exceeds the budget.")
        else:
            self._manager = manager
        self._name = name
        self._staff_list = []

    @property
    def manager(self):
        return self._manager

    @property
    def name(self):
        return self._name

    def add_staff(self, staff):
        curr_salary = self._manager.gross_salary() + sum(
            staff.gross_salary for staff in self._staff_list
        )
        if curr_salary + staff.gross_salary() > self._budget:
            raise StaffManagementException("Cannot add staff as budget will be exceeded.")
        elif staff.gross_salary() > self._manager.gross_salary():
            raise StaffManagementException("Staff has more salary than manager.")
        else:
            self._staff_list.append(Staff)
        return True


if __name__ == '__main__':
    # creating a manager
    m = Manager(1, 'Peter', 6000)
    print(m.salary, m.name, m.allowance(), m.gross_salary())
    # creating a department
    d = Department(15000,'Production', m)
    print(d.manager, d.name, d._budget)
    # creating support staff
    s = SupportStaff(2, 'John', 2000)
    # adding s to the staff list in d
    print(d.add_staff(s))