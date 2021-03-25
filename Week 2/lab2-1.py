from datetime import datetime

class Flight:
    def __init__(self, flight_no, destination, departure_date):
        self._flight_no = flight_no
        self._destination = destination
        self._departure_date = departure_date

    @property
    def flight_no(self):
        return self._flight_no

    @property
    def destination(self):
        return self._destination

    @property
    def departure_date(self):
        return self._departure_date

    @flight_no.setter
    def flight_no(self, flight_no):
        self._flight_no = flight_no

    @departure_date.setter
    def departure_date(self, departure_date):
        self._departure_date = departure_date

    def __str__(self):
        return '{} {} {:%d %b %Y %I:%M %p}'.format(self._flight_no, self._destination, self.departure_date)


class Passenger:
    def __init__(self, name: str, flight: Flight):
        self._name = name
        self._flight = flight

    @property
    def name(self):
        return self._name

    def change_flight(self, new_flight):
        self._flight = new_flight

    def __str__(self):
        return f"{self._name} {self._flight}"


if __name__ == '__main__':
    # create a Flight object - SQ1 to LA on 30/03/2019 at 0415
    f1 = Flight('SQ1', 'LA', datetime(2019, 3, 30, 4, 15))
    # create two Passenger object that takes f1
    p1 = Passenger('John', f1)
    p2 = Passenger('Mary', f1)
    # print passenger information using str method
    print(p1, p2, sep='\n')
    # change f1 departure date to 29/3/2019 at 1525
    f1.departure_date = datetime(2019, 3, 29, 15, 25)
    # print passenger information again using str method
    print(p1, p2, sep='\n')
