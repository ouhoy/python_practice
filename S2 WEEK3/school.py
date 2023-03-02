class School:
    def __init__(self, name: str, description: str, programs: list):
        self.__name = name
        self.__description = description
        self.__programs = programs

    def display(self):
        return {"name": self.__name, "description": self.__description, "programs": self.__programs}
