# 1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv
script_name, work_hours, salary_per_hour, award = argv

try:
    float(work_hours)
    float(salary_per_hour)
    float(award)
except ValueError:
    print(f"Ошибка, обнаружены не числовые значения! "
          f"Рабочих часов: {work_hours}, оплата в час: {salary_per_hour}, премия: {award}")
else:
    print(f"ЗП сотрудника составит: {float(work_hours) * float(salary_per_hour) + float(award)}")
