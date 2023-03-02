class Course:
    def __init__(self, title: str, hv: int, description: str):
        self.__title = title
        self.__hv = hv
        self.__description = description
        # self.__course_code = course_code
        # self.lecturer = lecturer

    def get_title(self):
        return self.__title

    def display(self):
        return {"title": self.__title, "hv": self.__hv, "description": self.__description}
