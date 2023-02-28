from person import Person


class Lecturer(Person):

    def __init__(self, firstname: str, lastname: str, lectured_courses: list):
        super().__init__(firstname, lastname)
        self.__lectured_courses = lectured_courses

    def add_course(self, new_course):
        self.__lectured_courses.append(new_course)

    def remove_course(self, course):
        if course in self.__lectured_courses:
            print(f"The course {course.get_title()} has been removed!")
            return self.__lectured_courses.remove(course)
        else:
            print(f"The course {course.get_title()} is not lectured by Mr/Ms {self.__firstname} {self.__lastname}")
