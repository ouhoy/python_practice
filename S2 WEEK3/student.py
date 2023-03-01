from person import Person


class Student(Person):
    def __init__(self, firstname: str, lastname: str, grade: int):
        super().__init__(firstname, lastname)
        self.__grade = grade
