class Name:
    def __init__(self, gender, first_name, last_name, middle_name):
        self._gender = gender.lower()
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self._first_name = new_first_name

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, new_middle_name):
        self._middle_name = new_middle_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name

    def get_full_name(self):
        return f"{'Mr' if self._gender == 'm' else 'Ms'} {self.first_name} {self.middle_name} {self.last_name}"

    def get_initials(self):
        return f"{self._first_name[0]}. {self._middle_name[0]}. {self._last_name[0]}"

    def __str__(self):
        return f"{self._gender} {self._first_name} {self._middle_name} {self._last_name}"


if __name__ == '__main__':
    n = Name('m', 'Kow Boon', 'Tan', 'Jerome')
    print(n)
    print(n.get_full_name())
    n.middle_name = 'Tommy'
    print(n.get_full_name())
    print(n.get_initials())
