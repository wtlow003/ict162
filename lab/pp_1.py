# Practise Paper QN 1
from datetime import datetime


class Course:

    def __init__(self, code, title, dev_cost):
        self._code = code
        self._title = title
        self._dev_cost = dev_cost

    @property
    def code(self):
        return self._code

    @property
    def dev_cost(self):
        return self._dev_cost

    def __str__(self):
        return f"Course Code: {self._code} Course Name: {self._title}"


class Instructor:

    def __init__(self, email, name, rate_per_day):
        self._email = email
        self._name = name
        self._rate_per_day = rate_per_day

    @property
    def email(self):
        return self._email

    @property
    def rate_per_day(self):
        return self._rate_per_day

    @rate_per_day.setter
    def rate_per_day(self, new_rate):
        self._rate_per_day = new_rate

    def __str__(self):
        return f"Instructor email: {self._email} Name: {self._name}"


class CourseSchedule:

    _sch_id = 1

    def __init__(self, course, instructor, start_date, duration):
        self._course = course
        self._instructor = instructor
        self._start_date = start_date
        self._duration = duration
        self._schedule_id = f"{course.code}_{type(self)._sch_id}"
        # increment for every course schedule created
        type(self)._sch_id += 1

    @classmethod
    def change_sch_id(cls, another_id):
        cls._sch_id = another_id

    @property
    def schedule_id(self):
        return self._schedule_id

    def course_fee(self):
        return self._course.dev_cost + (self._duration * self._instructor.rate_per_day)

    def get_course_code(self):
        return self._course.code

    def get_instructor_email(self):
        return self._instructor.email

    def __str__(self):
        return (f"Schedule Id: {self._schedule_id} "
                f"Start Date: {self._start_date.strftime('%d/%m/%Y')} "
                f"Duration: {self._duration} days"
                f"\n{self._course}"
                f"\n{self._instructor}")


if __name__ == '__main__':
    c = Course('PY214', 'Introduction to Python', 2000)
    i = Instructor('xxx@yyy.com', 'Joe Wong', 150)
    s = CourseSchedule(c, i, datetime(2020, 6, 1), 3)
    print(s)