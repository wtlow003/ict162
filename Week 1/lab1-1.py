class Name:
    def __init__(self, gender: str, last_name: str, first_name: str, middle_name: str):
        self._gender = gender.lower()
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    '''Getter, Setter method only available for last_name, first_name, middle_name'''
    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_name(self):
        return self._middle_name

    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name

    @first_name.setter
    def first_name(self, new_first_name):
        self._first_name = new_first_name

    @middle_name.setter
    def middle_name(self, new_middle_name):
        self._middle_name = middle_name

    def get_full_name(self):
        '''Method to return full name with a saluation "Mr." or "Mrs."'''
        salutation = f"{'Mr.' if self._gender == 'm' else 'Mrs.'}"
        return f"{salutation} {self._last_name} {self._first_name} {self._middle_name}"

    def get_initials(self):
        return f"{self._first_name[0]}. {self._middle_name[0]}. {self._last_name}"

    def __str__(self):
        return f"{self._gender} {self._last_name} {self._first_name} {self._middle_name}"


if __name__ == '__main__':
    n1 = Name('M', 'Low', 'Wei', 'Teck')
    n2 = Name('F', 'Tan', 'Jennifer', 'Xiaoyuan')
    print(n1.get_full_name(), n1.get_initials())
    print(n2.get_full_name(), n2.get_initials())
    print(n1)
    print(n2)
