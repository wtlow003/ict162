# defining a STUDENT class

class Student:
    # constructor: initialise the object
    def __init__(self, name, date_enrolled, contact, is_active, fee_owed=None):
        # defining instance variables
        # using underscore _ to define instance variable to not be access directly
        # if you __ (dunder), it will return an error if variable is accessed
        self._name = name.split()
        self._date_enrolled = date_enrolled
        self._contact = contact
        self._is_active = is_active
        self._fee_owed = 1000 if fee_owed is None else fee_owed

    # accessor methods
    @property
    def name(self):
        return " ".join(self._name)

    # mutator methods
    @name.setter
    def name(self, new_name):
        self._name = new_name.split()

    # accessor methods
    @property
    def date_enrolled(self):
        return self._date_enrolled

    @property
    def fee_owed(self):
        return self._fee_owed

    @fee_owed.setter
    def fee_owed(self, update_fees):
        if update_fees >= 0:
            self._fee_owed = update_fees
        else:
            self._fee_owed = 1000

    def __str__(self):
        return f"{self.name} {self.date_enrolled} {self._contact} {self._is_active}" +\
        f" {self.fee_owed}"


def main():
    student1 = Student("Jensen", "2021, 2, 1", 83058821, True)
    # before
    print(f"Before: {student1.name}, {student1._date_enrolled}")
    student1.name = "Thomas Bourbon"
    # after
    print(f"After: {student1.name}, {student1._date_enrolled}")
    print(student1.name)
    print(student1.fee_owed)
    student1.fee_owed -= 100
    student1.fee_owed = student1.fee_owed - 100
    print(student1.fee_owed)
    print(student1)


if __name__ == '__main__':
    main()
