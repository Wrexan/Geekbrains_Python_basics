# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника

vyr_usd = round(float(input("Введите прибыль фирмы: ")), 2)
zatr_usd = round(float(input("Введите затраты: ")), 2)

if zatr_usd < vyr_usd:
    print(f"У вас прибыльное предприятие\nРентабельность: {round(vyr_usd/zatr_usd, 2)}")
    people = int(input("Введите число сотрудников: "))
    print(f"Каждый сотрудник получит: {round((vyr_usd - zatr_usd) / people, 2)}")
else:
    print(f"Ваше предприятие убыточно")