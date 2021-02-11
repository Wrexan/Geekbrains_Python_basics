# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint
from functools import reduce
num_of_vars = 20
some_vars = [str(randint(0, 500)) for i in range(num_of_vars)]
data_file = "l05_hw5_text.txt"
errmsg = ["--Не удается создать файл: ", "--Не удается прочесть файл: "]
def sum_everything(ex, wy):	return ex + wy

try:
    with open(data_file, "w", encoding="utf-8") as f:
        f.write(" ".join(some_vars))
except IOError:
    print(f"{errmsg[0]}{data_file}")
try:
    with open(data_file, "r", encoding="utf-8") as f:
        data = f.read()
        if data:
            print(reduce(sum_everything, [int(i) for i in data.split(" ")]))
except (IOError, ValueError):
    print(f"{errmsg[1]}{data_file}")

