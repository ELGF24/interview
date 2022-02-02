class User:

    def __init__(self, name, lname):
        self.__name = name
        self.__lname = lname

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_lname(self):
        return self.__lname

    def set_lname(self, lname):
        self.__lname = lname