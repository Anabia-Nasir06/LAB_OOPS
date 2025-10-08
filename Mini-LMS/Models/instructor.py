from person import Person
from Management.studentlist import StudentList
from student import Student


class Instructor(Person):
    def __init__(self, name: str, id: str):
        super().__init__(name, id)
        self._students = StudentList()  # aggregation → instructor manages students

    @property
    def students(self):
        return self._students

    def assign_grade(self, student: Student, course_code: str, grade: str):
        course = student.courses.searchByCode(course_code)
        if course:
            print(f"Assigned grade '{grade}' to {student.name} for {course.name}")
        else:
            print(f"No course with code '{course_code}' found for {student.name}.")

    def view_student(self, seat_no: str):
        student = self._students.search_by_seat_no(seat_no)
        if student:
            print(student)
        else:
            print(f"No student found with seat number '{seat_no}'.")

    def __str__(self):
        return f"Instructor: {self.name} (ID: {self.id})"
