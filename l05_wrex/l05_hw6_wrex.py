# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

lessons_dict = {}
data_file = "l05_hw6_text.txt"
errmsg = ["--Не удается прочесть файл: ", "--Не найден разделитель ':' в строке: "]
eof = 0

try:
    with open(data_file, "r", encoding="utf-8") as f:
        while not eof:
            data_s = f.readline()
            if data_s:
                ind = data_s.find(":")
                if ind + 1:
                    data_fs = ""
                    for a in data_s:
                        if a.isdigit() or a == " ":
                            data_fs += a
                    data_l = "".join(i for i in data_s if i in " 0123456789").split()
                    lessons_dict.update({data_s[:ind+1]: sum(int(i) for i in data_l)})
                else:
                    print(f"{errmsg[1]}")
            else:
                eof = 1
        print(f"{lessons_dict}")
except IOError:
    print(f"{errmsg[0]}{data_file}")


