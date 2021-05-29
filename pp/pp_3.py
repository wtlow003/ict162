# Practise Paper Qn 3

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

    @property
    def start_date(self):
        return self._start_date

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


class TraininingProvider:

    def __init__(self, name):
        self._name = name
        self._course_schedules = {}

    def add_course_schedule(self, course, instructor, start_date, duration):
        course_sched = CourseSchedule(course, instructor, start_date, duration)
        course_sched_ids = self._course_schedules.keys()
        if course_sched.schedule_id in course_sched_ids:
            raise Exception("Course Schedule already added!")
        elif (start_date - datetime.now()).days < 10:
            raise Exception("start_date must be a least 10 days later than today.")
        elif duration < 1:
            raise Exception("Duration must be at least 1 day")
        else:
            self._course_schedules[course_sched.schedule_id] = course_sched

    def remove_course_schedule(self, course_schedule_id):
        course_sched_ids = self._course_schedules.keys()
        if course_schedule_id not in course_sched_ids:
            raise Exception("Course schedule Id not found!")
        elif (datetime.now() - self._course_schedules[course_schedule_id].start_date).days < 3:
            raise Exception("Course schedule start date too close to remove!")

    def __str__(self):
        return '\n'.join(str(item) for item in self._course_schedules.values())

if __name__ == '__main__':
    tp = TraininingProvider('Coding Ace Pte. Ltd.')
    print(tp)
    c = Course('PY214', 'Introduction to Python', 2000)
    i = Instructor('xxx@yyy.com', 'Joe Wong', 150)

    try:
        # fail as it does not start 10 days later
        # tp.add_course_schedule(c, i, datetime(2021, 5, 26), 3)
        # fail as it does not have at least 1 day
        # tp.add_course_schedule(c, i, datetime(2021, 6, 10), 0)
        # passed
        tp.add_course_schedule(c, i, datetime(2021, 6, 10), 1)
        print(tp)
        # trying to remove non-existent sched_id
        tp.remove_course_schedule('PY214_2')
    except Exception as e:
        print(e)