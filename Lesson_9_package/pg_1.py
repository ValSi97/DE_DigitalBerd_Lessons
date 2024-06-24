from datetime import datetime, date
class Human:
    __name: str
    __age: int
    __bdt: datetime

    def __init__(self, name='Иван', bdate = date(2000,1,1)):
        self.__name = name
        self.__bdt = bdate

    #def set_age(self, age):
    #    self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_bdate(self, bdate):
        self.__bdt = bdate

    def get_name(self):
        return self.__name

    def get_age(self):
        #return date.today() - self.__bdt
        today = date.today()
        return today.year - self.__bdt.year - ((today.month, today.day) < (self.__bdt.month, self.__bdt.day))

    def get_bdate(self):
        return self.__bdt


class Rota:
    __name: str
    __members: list

    def __init__(self, name='Rota 228'):
        self.__members = []

    def add_members(self, *members):
        self.__members += members

    def remove_members(self, *members):
        for member in members:
            if member in self.__members:
                self.__members.remove(member)

    def get_members(self):
        return self.__members


class Polk:
    __name: str
    __members: list

    def __init__(self, name='Polk 1'):
        self.__members = []

    def add_rotas(self, *members):
        self.__members += members

    def remove_rotas(self, *members):
        for member in members:
            if member in self.__members:
                self.__members.remove(member)

    def remove_humans(self, *humans):
        print('1')
        for human in humans:
            for rota in self.__members:
                if human in rota.get_members():
                    rota.remove_members(human)

    def get_human_members(self):
        humans = []
        for rota in self.__members:
            humans += rota.get_members()
        return humans



