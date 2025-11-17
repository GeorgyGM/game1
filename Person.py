from Section import Section
class Person:
    __section = set()
    def __init__(self, fio, phone):
        self.__fio = fio
        self.__phone = phone

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.__fio = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    def add_section(self, value):
        self.__section.add(value)

    def del_section(self, name):
        self.__section.discard(name)

    def __str__(self):
            return(f"fio: {self.__fio} | phone: {self.__phone} | {self.__section}")




if __name__ == '__main__':
    person = Person("fio", "12345")
    print(person)
    # print(person)
    print(person.fio)
    person.add_section("бокс")
    person.add_section("аэробика")
    print(person)