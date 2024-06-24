from datetime import datetime, timedelta, date

from Lesson_9_package.pg_1 import Human, Rota, Polk

dt = datetime.now()
print(dt)
dt = datetime.now() - timedelta(hours=1)
print(dt)

o_vasya = Human('Vasya', date(1990, 2, 2))
o_petya = Human('Petya', date(1980, 3, 3))
o_ivan = Human()

o_ivan.set_bdate(date(1979, 3, 14))

o_sasha = Human('Sasha')
o_dima = Human('Dima')
o_abu = Human('Abu')

print(o_vasya.get_name())
print(o_petya.get_name())
print(o_ivan.get_name())

print(o_vasya.get_age())
print(o_petya.get_age())
print(o_ivan.get_age())

print(o_vasya.get_bdate())
print(o_petya.get_bdate())
print(o_ivan.get_bdate())

o_rota1 = Rota('Rota 13')
o_rota1.add_members(o_vasya, o_petya, o_ivan)
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
