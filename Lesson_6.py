class Human:
    __hands: int
    __legs: int
    __ears: int
    __eyes: int
    __age: int
    __sex: int
    __name: str
    __speed: float

    def __init__(self, v_name, v_sex=1):
        self.__hands = 2
        self.__legs = 2
        self.__ears = 2
        self.__eyes = 2
        self.__age = 30
        self.__sex = v_sex
        self.__name = v_name
        self.__speed = 3.0

    def __str__(self):
        return self.__name + ' ' + str(self.__age) + ' ' + str(self.__speed)

    def get_info(self):
        return self.__name, self.__hands, self.__age, self.__ears, self.__eyes, self.__sex, self.__speed
        #print('\n')
        #print(f'Name = {str(self.__name)}')
        #print(f'Hands = {str(self.__hands)}')
        #print(f'Age = {str(self.__age)}')
        #print(f'Ears = {str(self.__ears)}')
        #print(f'Eyes = {str(self.__eyes)}')
        #print(f'Sex = {str(self.__sex)}')
        #print(f'speed = {str(self.__speed)}')


class Children(Human):
    __school: str
    __dad: Human
    __mom: Human
    __coord_x: float
    __coord_y: float

    def __init__(self, v_name='Шлёпа', v_school='Школа 1', o_dad=None, o_mom=None):
        super().__init__(v_name)
        self.__speed = 6.0
        self.__age = 10
        self.__school = v_school
        self.__dad = o_dad
        self.__mom = o_mom
        self.__coord_x = 0.0
        self.__coord_y = 0.0
    
    def __str__(self):
        return super().__str__()

    def get_info(self):
        return super().get_info(), self.__school, self.__dad, self.__mom
        #print(f'School = {str(self.__school)}')
        #print(f'Dad = {str(self.__dad)}')
        #print(f'Mom = {str(self.__mom)}')

    def get_coord_info(self):
        print('\n')
        print(f'Координата Х = {self.__coord_x}')
        print(f'Координата Y = {self.__coord_y}')

    def change_coord_info(self, f_coord_x, f_coord_y):
        self.__coord_x = f_coord_x
        self.__coord_y = f_coord_y


class Schoolbus:
    model: str
    num: str
    list_passengers: list

    def __init__(self, v_model = 'ПАЗ 228', v_num = 'o000oo'):
        self.model = v_model
        self.num = v_num
        self.list_passengers = []

    def get_info(self):
        print('\n')
        print(f'Bus params:')
        print(f'model: {self.model}')
        print(f'num: {self.num}')
        print(f'list_passengers:')
        for passenger in self.list_passengers:
            print(f' {passenger}')

    def add_passenger(self, o_passenger):
        print('\n')
        print(f'Добавление пассажира {o_passenger}')
        is_passenger = False

        for passenger in self.list_passengers:
            if passenger == o_passenger:
                is_passenger = True

        if not is_passenger:
            self.list_passengers.append(o_passenger)
            print ('Пассажир добавлен!')
        else:
            print('Пассажир не добавлен, т.к. уже присутствует!')

    def remove_passenger(self, o_passenger):
        print('\n')
        print(f'Удаление пассажира {o_passenger}')
        is_passenger = False

        for passenger in self.list_passengers:
            if passenger == o_passenger:
                is_passenger = True
                self.list_passengers.remove(o_passenger)
                print ('Пассажир удален!')
        if not is_passenger:
            print('Пассажир не удален, т.к. уже отсутствует!')

    def change_passengers_coords(self, coord_x, coord_y):
        for passenger in self.list_passengers:
            passenger.__coord_x = coord_x
            passenger.__coord_y = coord_y

        print('Координаты изменены!')


o_vasya = Human('Vasya',1)
o_masha = Human('Masha',0)

print(o_vasya)
print(o_vasya.get_info())

print(o_masha)
print(o_masha.get_info())

o_petya = Children('Петя','Школа 228', o_vasya, o_masha)
o_petya.change_coord_info(1.0,0.1)
o_sasha = Children('Саша','Школа 228', o_vasya, o_masha)
o_sasha.change_coord_info(2.0,0.2)
o_vanya = Children('Ваня','Школа 228', o_vasya, o_masha)
o_vanya.change_coord_info(3.0,0.3)
print(o_petya)
print(o_petya.get_info())
o_petya.get_coord_info()
print(o_sasha)
print(o_sasha.get_info())
o_sasha.get_coord_info()
print(o_vanya)
print(o_vanya.get_info())
o_vanya.get_coord_info()


o_schoolbus = Schoolbus()
o_schoolbus.get_info()
o_schoolbus.add_passenger(o_petya)
o_schoolbus.add_passenger(o_sasha)
o_schoolbus.add_passenger(o_vanya)
o_schoolbus.add_passenger(o_vanya)
o_schoolbus.get_info()

o_schoolbus.change_passengers_coords(228.0, 14.88)

o_petya.get_coord_info()
o_sasha.get_coord_info()
o_vanya.get_coord_info()




