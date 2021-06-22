# Practicse Paper QN 2
from abc import ABC, abstractmethod
from datetime import datetime
from pp_1 import Course, CourseSchedule, Instructor


class Reservation(ABC):

    _id = 1

    def __init__(self, cust_email, cust_name, course_schedule):
        self._reservation_id = type(self)._id
        self._cust_email = cust_email
        self._cust_name = cust_name
        self._course_schedule = course_schedule
        self._reservation_date = datetime.now()
        # increment of id
        type(self)._id += 1

    @abstractmethod
    def course_fee(self):
        pass

    def __str__(self):
        return (
            f"Reservation Id: {self._reservation_id} Email: {self._cust_email} "
            f"Name: {self._cust_name} Reservation Date: {self._reservation_date.strftime('%d/%m/%Y')}"
            f"{self._course_schedule}"
            f"\nCourse fee: {self.course_fee()}"
        )


class IndividualReservation(Reservation):

    _discount = 0.3

    def __init__(self, cust_email, cust_name, year_born, course_schedule):
        super().__init__(cust_email, cust_name, course_schedule)
        self._year_born = year_born

    def course_fee(self):
        # calculating age diff
        year_diff = datetime.now().year - self._year_born
        if year_diff >= 55:
            return self._course_schedule.course_fee() * (1 - type(self)._discount)
        return self._course_schedule.course_fee()


class CorporateReservation(Reservation):

    _discount = 0.5

    def __init__(self, cust_email, cust_name, company, course_schedule):
        super().__init__(cust_email, cust_name, course_schedule)
        self._company = company

    def course_fee(self):
        return self._course_schedule.course_fee() * (1 - type(self)._discount)


if __name__ == "__main__":
    # making a individual reservation without hitting discount age
    c = Course("PY214", "Introduction to Python", 2000)
    i = Instructor("xxx@yyy.com", "Joe Wong", 150)
    cs = CourseSchedule(c, i, datetime(2020, 6, 1), 3)
    ir = IndividualReservation("a@b.com", "John", 1950, cs)
    print(ir)
