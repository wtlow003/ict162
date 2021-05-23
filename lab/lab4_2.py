# LAB 4 Q2 (Exception Handling)

class InvalidAssessmentException(Exception):
    """Raise exception for violation of business rule in Asssessment"""

class InvalidAssesssmentDetailException(InvalidAssessmentException):

    def __init__(self, message, asssessment):
        super().__init__(message)
        self._assessment = asssessment

    @property
    def assessment(self):
        return self._assessment


class Assessment:

    _max = 100

    def __init__(self, id, mark):
        self._id = id
        self._mark = mark

    @property
    def id(self):
        return self._id

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, new_mark):
        self._mark = new_mark

    @classmethod
    def max_marks(cls):
        return cls._max

