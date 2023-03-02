class School:
    school_name = "sist"

    def __init__(self, name: str, description: str, programs: list):
        self.__name = name
        self.__description = description
        self.__programs = programs

    def display(self) -> dict:
        return {"name": self.__name, "description": self.__description, "programs": self.__programs}

    @staticmethod
    def get_school_name(cls):
        return cls.school_name
