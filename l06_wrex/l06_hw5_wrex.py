# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    title = "Канцелярщина"

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationary):
    def draw(self):
        print("Рисуем ручкой.")


class Pencil(Stationary):
    def draw(self):
        print("Рисуем карандашом.")


class Handle(Stationary):
    def draw(self):
        print("Рисуем маркером.")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
