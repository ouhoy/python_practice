class Person:
    def __init__(self, firstname: str, lastname: str):
        self.__firstname = firstname
        self.__lastname = lastname

    def get_fullname(self):
        return {"firstname": self.__firstname, "lastname": self.__lastname}

    def set_fullname(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname
        return {"firstname": self.__firstname, "lastname": self.__lastname}


class Student(Person):
    def __init__(self, firstname: str, lastname: str, age: int):
        super().__init__(firstname, lastname)
        self.__age = age


class Lecturer(Person):
    def __init__(self, firstname: str, lastname: str, list_of_courses_lectured: list):
        super().__init__(firstname, lastname)
        self.firstname = firstname
        self.lastname = lastname
        self.list_of_courses_lectured = list_of_courses_lectured


class Program:
    def __init__(self, name: str, list_of_courses: list):
        self.name = name
        self.list_of_courses = list_of_courses


class Course:
    def __init__(self, title: str, hv: int, description: str):
        self.__title = title
        self.__hv = hv
        self.__description = description

    def get_title(self):
        return self.__title


student_one = Student("Abdallah", "Dahmou", 23)
course_one = Course("Developing Quality Software and Systems", 30, "Building high-quality software systems.")
lecturer_one = Lecturer("Younes", "El Amr-ani", ["Developing Quality Software", "Introduction to Programming"])

print(student_one.get_fullname())
