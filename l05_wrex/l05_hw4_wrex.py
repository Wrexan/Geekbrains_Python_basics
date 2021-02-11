# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

lines = ""
numbers_ru = [["1", "Один"],
              ["2", "Два"],
              ["3", "Три"],
              ["4", "Четыре"],
              ["5", "Пять"],
              ["6", "Шесть"],
              ["7", "Семь"],
              ["8", "Восемь"],
              ["9", "Девять"]]
ioerr = ["--Can't read file: ", "--Can't create/open file: "]
data_file = ["l05_hw4_text.txt", "l05_hw4_out.txt"]
eof = i = 0
try:
    with open(data_file[0], "r", encoding="utf-8") as f:
        while not eof:
            line = f.readline()
            if line:
                li = line.split()
                lines = f'{(lines + "".join([a[1] for a in numbers_ru if a[0] == li[2]]  or li[0]))} {li[1]} {li[2]}\n'
                i += 1
            else:
                eof = 1
        print(lines)
    try:
        with open(data_file[1], "w") as f:
            f.write(lines)
    except IOError:
        print(f'{ioerr[1]}{data_file[1]}')
except IOError:
    print(f"{ioerr[0]}{data_file[0]}")
