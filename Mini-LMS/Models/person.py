class Person:
    def __init__(self, name: str, id: str):
        self.__name = name
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not value:
            raise ValueError("ID cannot be empty.")
        self.__id = value

    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__id}"
