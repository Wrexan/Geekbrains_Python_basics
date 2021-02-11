# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

firms_profitable = {}
firms_looser = {}
data_file = ["l05_hw7_text.txt", "l05_hw7_text.json"]
errmsg = ["--Не удается прочесть файл: ", "Не удалось обработать строку: "]
eof = profit_full = loose_fool = 0

try:
    with open(data_file[0], "r", encoding="utf-8") as f:
        while not eof:
            data_s = f.readline()
            if data_s:
                ind_3 = data_s.rfind(' ', 0, len(data_s))  # Minus-len(data_s)
                ind_2 = data_s.rfind(' ', 0, ind_3)  # Plus
                ind_1 = data_s.rfind(' ', 0, ind_2)  # Name
                try:
                    profit = float(data_s[ind_2+1:ind_3]) - float(data_s[ind_3+1:])
                    if profit > 0:
                        firms_profitable.update({data_s[ind_1 + 1:ind_2] + ' "' + data_s[:ind_1] + '"': profit})
                        profit_full += profit
                    else:
                        firms_looser.update({data_s[ind_1 + 1:ind_2] + ' "' + data_s[:ind_1] + '"': profit})
                        loose_fool += profit
                except ValueError:
                    print(f"{errmsg[1]}{data_s}")
            else:
                eof = 1
        listik = [firms_profitable, {"average_profit": profit_full}, firms_looser, {"average_loose": loose_fool}]
        print(listik)
        try:
            with open(data_file[1], "w", encoding="utf-8") as w:
                w.write(str(listik))
        except IOError:
            print(f"{errmsg[0]}{data_file[1]}")
except IOError:
    print(f"{errmsg[0]}{data_file[0]}")


