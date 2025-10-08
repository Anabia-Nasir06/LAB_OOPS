from Models.course import Course

class CourseList:
    def __init__(self, size: int = 50):
        self._courses = []
        self._count = 0
        self._size = size

    @property
    def courses(self):
        return self._courses.copy()

    @property
    def count(self):
        return self._count

    @property
    def size(self):
        return self._size

    def addCourse(self, course):
        if self._count >= self._size:
            print("Course list is full.")
            return

        for c in self._courses:
            if c.code == course.code:
                print("Course with this code already exists.")
                return

        self._courses.append(course)
        self._count += 1
        print(f"Course {course.name} added successfully.")

    def removeCourse(self, code: str):
        for c in self._courses:
            if c.code == code:
                self._courses.remove(c)
                self._count -= 1
                print(f"Course {c.name} removed successfully.")
                return
        print("Course not found.")

    def searchByName(self, name: str):
        for c in self._courses:
            if c.name == name:
                return c
        return None

    def searchByCode(self, code: str):
        for c in self._courses:
            if c.code == code:
                return c
        return None

    def __str__(self):
        text = "Course List:\n"
        for c in self._courses:
            text += str(c) + "\n"
        return text
