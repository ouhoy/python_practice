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
