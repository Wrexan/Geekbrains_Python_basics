# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
how_many_switches = 6


class TrafficLight:
    switch: int = 0
    light_states = ('Red', 7, 'Yellow', 2, 'Green', 3)
    __color = 'Yellow'

    def running(self):
        self.__color = self.light_states[self.switch]
        print(self.__color)
        time.sleep(self.light_states[self.switch + 1])
        self.switch = self.switch + 2 if self.switch < 3 else 0
        return self.switch / 2


col = oldcol = 0
firstrun = 1
svetik = TrafficLight()

for i in range(how_many_switches):
    col = svetik.running()
    if firstrun:
        firstrun = 0
        oldcol = col - 1
    if not (col == oldcol + 1 or col == oldcol - 2):
        print(col, oldcol)
        print('Сбой в работе светофора')
        break
    else:
        oldcol = col
