class Person:
    def __init__(self, firstname: str, lastname: str):
        self.__firstname = firstname.capitalize()
        self.__lastname = lastname.capitalize()

    def get_fullname(self):
        return {"firstname": self.__firstname, "lastname": self.__lastname}

    def set_fullname(self, firstname: str, lastname: str):
        self.__firstname = firstname.capitalize()
        self.__lastname = lastname.capitalize()
        return {"firstname": self.__firstname, "lastname": self.__lastname}
