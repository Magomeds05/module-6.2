class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color


    def get_model(self,__model):
        print(f'Модель:{__model}')

    def get_horsepower(self,__engine_power):
        print(f'Мощность двигателя:{__engine_power}')

    def get_color(self,__color):
        print(f'Цвет:{__color}')

    def print_info(self, get_model, get_horsepower, get_color):
        print(f' {get_model}, {get_horsepower}, {get_color}, Владелец:')

    def set_color(self,new_color):
        if new_color == self.__COLOR_VARIANTS:
            print()
        else:
            print(f'Нельзя сменить цвет на {new_color}')




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info('Porshe Macan', 710,'purple')

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info('Toyota Supra', 310, 'pink')