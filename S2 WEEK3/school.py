class School:
    def __init__(self, name: str, programs: list):
        self.__name = name
        self.__programs = programs

    def display(self):
        return {"name": self.__name, "programs": self.__programs}
