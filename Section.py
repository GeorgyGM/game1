class Section:
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity


    def __str__(self):
        return f"{self.__name} | {self.__quantity}"