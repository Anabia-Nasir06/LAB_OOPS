from Models.student import Student

class StudentList:
    def __init__(self, other=None, capacity: int = 2):
        if other is None:
            # Normal constructor
            self.__capacity = capacity
            self.__count = 0
            self.__students = [None] * self.__capacity
        else:
            # Deep copy constructor
            self.__capacity = other.__capacity
            self.__count = other.__count
            self.__students = [
                Student(s.name, s.id, s.seatNo) if s else None
                for s in other.__students
                    ]


    def add_student(self, student):
        """Add a student, resizing the list if needed."""
        if self.__count == self.__capacity:
            self.__resize()

        if self.__is_duplicate(student):
            print(f"Student with ID {student.id} already exists.")
            return

        self.__students[self.__count] = student
        self.__count += 1
        print(f"Student '{student.name}' added successfully.")

    def __is_duplicate(self, student):
        """Check if student already exists by ID."""
        for s in self.students:
            if s.id == student.id:
                return True
        return False

    def __resize(self):
        """Double the capacity of the list."""
        new_capacity = self.__capacity * 2
        new_students = [None] * new_capacity
        for i in range(self.__count):
            new_students[i] = self.__students[i]
        self.__students = new_students
        self.__capacity = new_capacity

    def remove_student(self, seat_no: str):
        """Remove student by seat number."""
        for i in range(self.__count):
            if self.__students[i] and self.__students[i].seatNo == seat_no:
                removed = self.__students[i]
                for j in range(i, self.__count - 1):
                    self.__students[j] = self.__students[j + 1]
                self.__students[self.__count - 1] = None
                self.__count -= 1
                print(f"Student '{removed.name}' removed successfully.")
                return
        print("Student not found.")

    def search_by_name(self, name: str):
        """Return student by name, or None if not found."""
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None

    def search_by_seat_no(self, seat_no: str):
        """Return student by seat number, or None if not found."""
        for s in self.students:
            if s.seatNo == seat_no:
                return s
        return None

    def sort_by_name(self):
        """Sort students alphabetically by name."""
        self.__students = sorted(
            [s for s in self.students if s],
            key=lambda s: s.name
        )
        self.__count = len(self.__students)
        self.__capacity = max(self.__capacity, self.__count)
        self.__students += [None] * (self.__capacity - self.__count)

    @property
    def students(self):
        """Return the list of valid students."""
        return [s for s in self.__students if s is not None]

    @property
    def count(self):
        return self.__count

    @property
    def capacity(self):
        return self.__capacity

    def __str__(self):
        if not self.students:
            return "No students in the list."
        text = "Student List:\n"
        for s in self.students:
            text += f"- {s.name} (Seat No: {s.seatNo}, ID: {s.id})\n"
        return text
