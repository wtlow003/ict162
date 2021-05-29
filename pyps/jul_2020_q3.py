from abc import ABC, abstractmethod

# Q3(a)


class EventException(Exception):
    """Exception class for exceptions raised for Events"""


# Q3(b)
class Event(ABC):

    _max_size = 15

    def __init__(self, venue):
        self._venue = venue
        self._participant_count = 0

    @classmethod
    def max_size(cls):
        return cls._max_size

    @property
    def venue(self):
        return self._venue

    @abstractmethod
    def event_cost(self):
        pass

    def add_participant(self):
        if (self._participant_count + 1) > type(self)._max_size:
            raise EventException("Cannot add participant. "
                                 "Number of participants is already at maximum")
        self._participant_count += 1

    def remove_participant(self):
        if (self._participant_count - 1) < 0:
            raise EventException("Cannot remove participant. "
                                 "Number of participants is already 0.")
        self._participant_count -= 1

    def __str__(self):
        return (f"Event Cost: ${self.event_cost()} {self._venue}\n"
                f"Participant count: {self._participant_count} max size: {self.max_size()}")


# Q3(c)
class Talk(Event):

    _max_size = 40

    def __init__(self, venue, venue_cost):
        super().__init__(venue)
        self._venue_cost = venue_cost

    def event_cost(self):
        return self._venue_cost + (5.5 * self._participant_count)

    def __str__(self):
        return (f"Venue cost: ${self.event_cost():.0f} {super().__str__()}")


# Q3(d)
class Visit(Event):

    @classmethod
    def max_size(cls):
        return 20

    def event_cost(self):
        return 10 * self._participant_count


# Q3(e)(i)
t = Talk('Orchid Hall', 800)
print(t)

# Q3(e)(ii)
class Menu:

    def __init__(self, event):
        self._event = event

    def option_1(self):
        try:
            self._event.add_participant()
        except EventException as e:
            print(e)
        finally:
            print(self._event)

    def option_2(self):
        try:
            self._event.remove_participant()
        except EventException as e:
            print(e)
        finally:
            print(self._event)

    def menu(self):
        print("Menu")
        print("1. Add Participants")
        print("2. Remove Participants")
        print("0. Exit")

        try:
            select_input = input("Enter options: ")
            if int(select_input) == 1:
                self.option_1()
            elif int(select_input) == 2:
                self.option_2()
            elif int(select_input) == 0:
                print("Program ends")
                exit()
            else:
                print("Invalid option")
        except ValueError:
            print(f"{select_input} is not a valid menu option")

if __name__ == '__main__':
    menu = Menu(t)

    while True:
        menu.menu()
        print()
