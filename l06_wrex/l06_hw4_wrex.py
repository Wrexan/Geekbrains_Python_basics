# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
from os import system as sys, name as os_name
from time import sleep

cls = 'cls' if os_name == 'nt' else 'clear'
autos = ['Volkswagen', 'Audi', 'BMW', 'Mercedes', 'Toyota', 'KIA', 'Tavria']
types = ['городский', 'спортивний', 'рабочий', 'полицейский']
colors = ['белый', 'чёрный', 'красный', 'синий', 'жёлтый', 'зелёный']
controls = [['налево', 'газ', 'направо', 'тормоз', 'изм.цвет',
             'изм.марку', 'изм.тип', 'выход'], [1, 2, 3, 4, 5, 6, 7, 0]]
greetings = ["--------- Добро пожаловать в наш виртуальный автосалон ---------", "--------- Всего доброго ---------"]
violations = persecutors = 0


class Car:
    name = 'Default'
    color = 'Default'
    speed = 0
    is_police = False
    type = 0

    def go(self, speed=0):
        if speed:
            print(f'{types[self.type]} {self.color} {self.name} разгоняется'.capitalize(), end="")
        elif self.speed:
            print(f'{types[self.type]} {self.color} {self.name} продолжает движение'.capitalize(), end="")
        else:
            print(f'{types[self.type]} {self.color} {self.name} стоит'.capitalize(), end="")
        self.speed += speed

    def stop(self):
        print(f'{types[self.type]} {self.color} {self.name} остановился'.capitalize())
        self.speed = 0

    def turn(self, turn=0):
        print(f'{types[self.type]} {self.color} {self.name} повернул направо'.capitalize(), end="") \
            if turn else print(f'{types[self.type]} {self.color} {self.name} повернул налево'.capitalize(), end="")

    def show_speed(self):
        print(f' на скорости: {self.speed}км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f' на скорости: {self.speed}км/ч')
        if self.speed > 60: print('Вы превысили скорость!!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f' на скорости: {self.speed}км/ч')
        if self.speed > 40:
            print('Вы превысили скорость!!!')


class PoliceCar(Car):
    pass


def get_type():
    sys(cls)
    print(f'1){types[0]} 2){types[1]} 3){types[2]} 4){types[3]}')
    s = input(f'Выберите тип авто: ')
    try:
        t = int(s) - 1
    except ValueError:
        t = 0
    if t == 0:
        return TownCar(), t
    elif t == 1:
        return SportCar(), t
    elif t == 2:
        return WorkCar(), t
    else:
        return PoliceCar(), 3


def get_manuf():
    sys(cls)
    print(f'1){autos[0]} 2){autos[1]} 3){autos[2]} 4){autos[3]} 5){autos[4]} 6){autos[5]} 7){autos[6]}')
    try:
        i = int(input(f'Выберите марку авто: ')) - 1
        return i if i in range(len(autos)) else 0
    except ValueError:
        return 0


def get_color():
    sys(cls)
    print(f'1){colors[0]} 2){colors[1]} 3){colors[2]} 4){colors[3]} 5){colors[4]} 6){colors[5]}')
    try:
        i = int(input(f'Выберите цвет авто: ')) - 1
        return i if i in range(len(colors)) else 0
    except ValueError:
        return 0


def show_control():  # 'налево', 'газ', 'направо', 'тормоз', 'изм.цвет', 'изм.марку', 'изм.тип', 'выход'
    sys(cls)
    print(f'{controls[1][0]}){controls[0][0]} {controls[1][1]}){controls[0][1]} '
          f'{controls[1][2]}){controls[0][2]} {controls[1][3]}){controls[0][3]} '
          f'{controls[1][4]}){controls[0][4]} {controls[1][5]}){controls[0][5]} '
          f'{controls[1][6]}){controls[0][6]} | {controls[1][7]}){controls[0][7]}')


def get_control():  # 'налево', 'газ', 'направо', 'тормоз', 'изм.цвет', 'изм.марку', 'изм.тип', 'полицейский', 'выход'
    try:
        i = int(input(f'Ожидаем ваших команд: '))
        return i if i in controls[1] else 0
    except ValueError:
        return 8


# print(end=''.join('\b' for i in range(len(words))))

sys(cls)
print(greetings[0])
sleep(1)
MyCar, MyCar.type = get_type()
if MyCar.type == 3: MyCar.is_police = True

MyCar.name = autos[get_manuf()]
MyCar.color = colors[get_color()]
in_control = 8
# '1налево', '2газ', '3направо', '4тормоз', '5изм.цвет', '6изм.марку', '7изм.тип', '8полицейский', '0выход'
while True:
    show_control() if in_control in [0, 1, 2, 3, 4, 8] else 0
    if in_control == 1: MyCar.turn(0); MyCar.show_speed()
    if in_control == 2: MyCar.go(20); MyCar.show_speed()
    if in_control == 3: MyCar.turn(1); MyCar.show_speed()
    if in_control == 4: MyCar.stop()
    if in_control == 5: MyCar.color = colors[get_color()]; show_control(); MyCar.go(); MyCar.show_speed()
    if in_control == 6: MyCar.name = autos[get_manuf()]; show_control(); MyCar.go(); MyCar.show_speed()
    if in_control == 7:
        t_name, t_color, t_speed = MyCar.name, MyCar.color, MyCar.speed
        # MyCar.stop()
        del MyCar
        MyCar, MyCar.type = get_type()
        MyCar.name, MyCar.color, MyCar.speed = t_name, t_color, t_speed
        if MyCar == PoliceCar: MyCar.is_police = True
        show_control()
        MyCar.go()
        MyCar.show_speed()
    if in_control == 8: MyCar.go(0); MyCar.show_speed()
    if in_control == 0:
        MyCar.stop()
        del MyCar
        # sys(cls)
        print(greetings[1])
        break
    in_control = get_control()
