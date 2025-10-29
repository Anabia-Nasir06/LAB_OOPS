from Management.studentlist import StudentList
from Models.student import Student
from Management.courselist import CourseList
from Models.course import Course


class App:
    def __init__(self):
        self.students = StudentList()
        self.courses = CourseList()

    def run(self):
        while True:
            print("\n=== Learning Management System ===")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Show All Students")
            print("4. Enroll Student in Course")
            print("5. Drop Course from Student")
            print("6. Find Student by Name")
            print("7. Find Student by Seat No")
            print("8. Sort Students by Name")
            print("9. Sort Students by Seat No")
            print("10. Exit")

            choice = input("Choose an option: ")

            match choice:
                case "1":
                    self.add_students()
                case "2":
                    self.remove_student()
                case "3":
                    self.show_students()
                case "4":
                    self.enroll_course_to_student()
                case "5":
                    self.drop_course_from_student()
                case "6":
                    self.search_student_by_name()
                case "7":
                    self.search_student_by_seat()
                case "8":
                    self.students.sort_by_name()
                    print("Students sorted by name.")
                case "9":
                    self.students.sort_by_seat_no()
                    print("Students sorted by seat number.")
                case "10":
                    print("Exiting LMS. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def add_students(self):
        try:
            n = int(input("How many students to add? "))
        except ValueError:
            print("Invalid input.")
            return

        for i in range(n):
            print(f"\n--- Student {i+1} ---")
            name = input("Enter student name: ")
            seat_no = input("Enter seat number: ")
            student = Student(name, seat_no)

            try:
                course_count = int(input("How many courses to add? "))
            except ValueError:
                course_count = 0

            for j in range(course_count):
                cname = input(f"  Course {j+1} name: ")
                ccode = input(f"  Course {j+1} code: ")

                course = self.courses.searchByCode(ccode)
                if not course:
                    course = Course(name, code)
                    self.courses.addCourse(course)

                student.enroll_course(course)

            self.students.add_student(student)
            print(f"Student '{student.name}' added successfully.")

    def remove_student(self):
        seat_no = input("Enter seat number of student to remove: ")
        self.students.remove_student(seat_no)

    def show_students(self):
        if not self.students.students:
            print("No students available.")
            return

        print("\nStudent List:")
        for student in self.students.students:
            print(student)
            print("  Courses:", [c.name for c in student.courses.courses])

    def enroll_course_to_student(self):
        seat_no = input("Enter student seat number: ")
        student = self.students.search_by_seat_no(seat_no)
        if not student:
            print("Student not found.")
            return

        cname = input("Enter course name: ")
        ccode = input("Enter course code: ")

        course = self.courses.searchByCode(ccode)
        if not course:
            course = Course(cname, ccode)
            self.courses.addCourse(course)

        student.enroll_course(course)
        print(f"Course '{course.name}' added to student '{student.name}'.")

    def drop_course_from_student(self):
        seat_no = input("Enter student seat number: ")
        student = self.students.search_by_seat_no(seat_no)
        if not student:
            print("Student not found.")
            return

        ccode = input("Enter course code to remove: ")
        course = student.courses.searchByCode(ccode)
        if course:
            student.drop_course(ccode)
            print(f"Course '{course.name}' removed from student '{student.name}'.")
        else:
            print(f"Course with code '{ccode}' not found for this student.")

    def search_student_by_name(self):
        name = input("Enter name to search: ")
        student = self.students.search_by_name(name)
        if student:
            print("Found:", student)
            print("Courses:", [c.name for c in student.courses.courses])
        else:
            print("Student not found.")

    def search_student_by_seat(self):
        seat_no = input("Enter seat number: ")
        student = self.students.search_by_seat_no(seat_no)
        if student:
            print("Found:", student)
            print("Courses:", [c.name for c in student.courses.courses])
        else:
            print("Student not found.")


