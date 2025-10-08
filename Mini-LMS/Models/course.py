class Course:
    def __init__(self, name: str, code: str, capacity: int = 30):
        self.__name = name
        self.__code = code
        self.__capacity = capacity
        self.__students = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Course name cannot be empty.")
        self.__name = value

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value: str):
        if not value:
            raise ValueError("Course code cannot be empty.")
        self.__code = value

    @property
    def capacity(self):
        return self.__capacity

    @property
    def students(self):
        return self.__students

    def __str__(self):
        return f"Course: {self.__name} (Code: {self.__code})"
