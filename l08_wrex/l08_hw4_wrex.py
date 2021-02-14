# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class OfficeEquipmentStock:
    pass


class OfficeEquipment:
    def __init__(self, mass, cost, size, color):
        self.mass = mass; self.cost = cost; self.size = size; self.color = color


class Printer(OfficeEquipment):
    def __init__(self, mass, cost, size, color, is_laser=True, consumables='powder ink'):
        super().__init__(mass, cost, size, color)
        self.is_laser = is_laser
        self.consumables = consumables


class Scanner(OfficeEquipment):
    def __init__(self, mass, cost, size, color, work_size=20, speed=0):
        super().__init__(mass, cost, size, color)
        self.work_size = work_size
        self.speed = speed


class Copier(OfficeEquipment):
    def __init__(self, mass, cost, size, color, consumables='powder ink', work_size=20, speed=0):
        super().__init__(mass, cost, size, color)
        self.work_size = work_size
        self.speed = speed
        self.consumables = consumables

