class Module:

    _valid_start_character_of_code = ['B', 'E', 'I', 'S']

    def __init__(self, code, level):
        if code[0] not in type(self)._valid_start_character_of_code:
            self._code = type(
                self)._valid_start_character_of_code[0] + code[1:]
        else:
            self._code = code
        self._level = level

    @property
    def code(self):
        return self._code

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        self._level = new_level

    def change_level_by(self, change_by_level):
        if change_by_level > 0:
            self._level += change_by_level
        else:
            self._level -= abs(change_by_level)

        if self._level > 5:
            self._level = 5
        elif self._level < 0:
            self._level = 1

    def get_difference_in_levels(self, module):
        return self._level - module.level

    @classmethod
    def add_valid_start_character(cls, start_character):
        cls._valid_start_character_of_code.append(start_character)

    @classmethod
    def remove_valid_start_character(cls, start_character):
        cls._valid_start_character_of_code.remove(start_character)

    def __str__(self):
        return f"Code: {self._code} Level: {self._level}"


if __name__ == '__main__':
    # Q1(c)(i)
    m1 = Module('S123', 3)
    m2 = Module('B231', 2)

    # Q1(c)(ii)
    # changing level of m1 by 2 and set m2 to 1
    m1.change_level_by(2)
    m2.level = 1

    # Q1(c)(iii)
    # get difference in level
    print(m1.get_difference_in_levels(m2))

    # Q1(c)(iv)
    m1.add_valid_start_character('T')
