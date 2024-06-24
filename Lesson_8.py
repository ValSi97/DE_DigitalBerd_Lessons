class Human:
    __name: str
    __age: int

    def __init__(self, name='Иван', age=20):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

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

    def remove_humans(self,*humans):
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

o_vasya = Human('Vasya',18)
o_petya = Human('Petya',30)
o_ivan = Human()

o_sasha = Human('Sasha',50)
o_dima = Human('Dima',88)
o_abu = Human('Abu')

print(o_vasya.get_name())
print(o_petya.get_name())
print(o_ivan.get_name())

print(o_vasya.get_age())
print(o_petya.get_age())
print(o_ivan.get_age())

o_rota1 = Rota('Rota 13')
o_rota1.add_members(o_vasya,o_petya,o_ivan)
for member in o_rota1.get_members():
    print(member.get_name(), member.get_age())

o_rota2 = Rota('Rota 228')
o_rota2.add_members(o_sasha, o_dima, o_abu)
for member in o_rota2.get_members():
    print(member.get_name(), member.get_age())
    
o_polk1 = Polk()
print('добавляем роты в полк')
o_polk1.add_rotas(o_rota1, o_rota2)
print('выводим список людей в полку')
for human in o_polk1.get_human_members():
    print(human.get_name(), human.get_age())

o_polk1.remove_rotas(o_rota1)
print('выводим список людей в полку 2')
for human in o_polk1.get_human_members():
    print(human.get_name(), human.get_age())

o_polk1.add_rotas(o_rota1)
o_polk1.remove_humans(o_vasya, o_ivan)

print('выводим список людей в роте1')
for member in o_rota1.get_members():
    print(member.get_name(), member.get_age())
print('выводим список людей в роте2')
for member in o_rota2.get_members():
    print(member.get_name(), member.get_age())

print('выводим список людей в полку 3')
for human in o_polk1.get_human_members():
    print(human.get_name(), human.get_age())


