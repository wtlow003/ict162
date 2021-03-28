class Phone:
    def __init__(self, number: int):
        self._number = number
        self._speed_dial = [0] * 10

    def assign_speed_dial(self, digit, number):
        if digit >= 0 and digit <= 9:
            self._speed_dial[digit] = number
            return True
        else:
            return False

    def speed_dial(self, digit):
        if digit >= 0 and digit <= 9:
            if not self._speed_dial[digit]:
                return "No number assigned"
            else:
                return f"calling {self._speed_dial[digit]}"
        else:
            return "Invalid digit"

    def display_all_speed_dial(self):
        return '\n'.join(f'{idx} - not assigned' if val == 0 else f'{idx} - {val}' for idx, val in enumerate(self._speed_dial))

    def __str__(self):
        return f"{self._number, self._speed_dial}"


if __name__ == '__main__':
    p1 = Phone(830588821)
    print(p1)
    # assigning a speed dial number
    p1.assign_speed_dial(9, 67695503)
    # speed dial 9
    print(p1.speed_dial(9))
    print(p1.speed_dial(10))
    print(p1.speed_dial(1))
    print(p1.display_all_speed_dial())
