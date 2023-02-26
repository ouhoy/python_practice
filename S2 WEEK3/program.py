class Program:
    courses_list = []
    students_list = []

    def __init__(self, name: str, courses: list, students: list):
        self.name = name
        self.__courses = courses
        self.__students = students

        self.students_list.extend(self.__students)
        self.courses_list.extend(self.__courses)

    def get_students(self):
        return self.__students

    def add_student(self, new_student):
        self.students_list.append(new_student)

    def add_course(self, new_course):
        self.courses_list.append(new_course)
