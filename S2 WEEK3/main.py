from person import Person
from program import Program


class Student(Person):
    def __init__(self, firstname: str, lastname: str, age: int):
        super().__init__(firstname, lastname)
        self.__age = age


class Lecturer(Person):
    def __init__(self, firstname: str, lastname: str, list_of_courses_lectured: list):
        super().__init__(firstname, lastname)
        self.list_of_courses_lectured = list_of_courses_lectured


class Course:
    def __init__(self, title: str, hv: int, description: str):
        self.__title = title
        self.__hv = hv
        self.__description = description
        # self.lecturer = lecturer

    def get_title(self):
        return self.__title


student_one = Student("Abdallah", "Dahmou", 23)
student_two = Student("Rania", "Samih", 22)

course_one = Course("Developing Quality Software and Systems", 30, "Building high-quality software systems.")
course_two = Course("Web development", 25, "Building web applications with NodeJS and ReactJS.")

lecturer_one = Lecturer("Younes", "El Amr-ani", [course_one])

SE = Program("Software Engineering", [course_one, course_two], [student_one])
BA = Program("Business Management", [course_one], [student_two])

for num, student in enumerate(SE.get_students()):
    first_name = student.get_fullname()["firstname"]
    last_name = student.get_fullname()["lastname"]

    print(f"{num + 1} - {first_name} {last_name}")
