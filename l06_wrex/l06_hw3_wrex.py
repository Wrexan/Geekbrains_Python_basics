# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

salary = {'wage': 2000, 'bonus': 500}


class Worker:
    name = 'Васа'
    surname = 'Пупкен'
    position = 'Мистэр презыденс'
    _income = salary


class Position(Worker):
    def get_full_name(self): return f'{self.name} {self.surname}'

    def get_total_income(self): return int(self._income.get('wage')) + int(self._income.get('bonus'))


staff_1 = Position()

print(f'{staff_1.get_full_name()} из {staff_1.position}')
print(f'його зарплатня складає: {staff_1.get_total_income()}')
