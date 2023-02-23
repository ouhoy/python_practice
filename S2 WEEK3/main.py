class Person:
    def __init__(self, firstname: str, lastname: str, list_of_courses: list):
        self.firstname = firstname
        self.lastname = lastname
        self.list_of_courses = list_of_courses

    def get_name(self):
        print(self.firstname)


class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class Course:
    def __init__(self, title, hv, description):
        self.title = title
        self.hv = hv
        self.description = description


class Lecturer:
    def __init__(self, firstname, lastname, list_of_courses_lectured):
        self.firstname = firstname
        self.lastname = lastname
        self.list_of_courses_lectured = list_of_courses_lectured


studentOne = Student("Abdallah", "Dahmou", 23)

print(studentOne.firstname)
