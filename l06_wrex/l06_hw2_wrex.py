# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass=25, thickness=1):
        return self._length * self._width * mass * thickness


def calc_mass_from_list(l_w_m_t=None):
    if l_w_m_t is None:
        l_w_m_t = [0, 0, 0, 0]
    road_p = Road(l_w_m_t[0], l_w_m_t[1])
    return f'{l_w_m_t[0]}м * {l_w_m_t[1]}м * {l_w_m_t[2]}кг * {l_w_m_t[3]}см = {road_p.calc_mass(l_w_m_t[2], l_w_m_t[3])} т'


road_p1 = [1000, 5, 25, 1]
road_p2 = [2010, 25, 30, 5]

print(calc_mass_from_list(road_p1))
print(calc_mass_from_list(road_p2))
