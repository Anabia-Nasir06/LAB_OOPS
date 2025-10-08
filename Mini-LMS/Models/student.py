from Models.person import Person
from Management.courselist import CourseList

class Student(Person):
    def __init__(self, name: str, id: str, seat_no: str):
        super().__init__(name, id)        # call Person constructor
        self.__seat_no = seat_no
        self.__courses = CourseList()    # composition → student owns a list of courses

    @property
    def seatNo(self):
        return self.__seat_no

    @property
    def courses(self):
        """Return this student’s course list object."""
        return self.__courses

    def enroll_course(self, course):
        """Add a course to student’s course list."""
        self.__courses.add_course(course)

    def drop_course(self, code: str):
        """Remove a course from student’s course list."""
        self.__courses.remove_course(code)

    def __str__(self):
        return f"Student(Name: {self.name}, Seat No: {self.__seat_no})"
