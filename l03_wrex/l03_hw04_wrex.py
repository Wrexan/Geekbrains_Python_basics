# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_a(arg_a, arg_b):
    if str(arg_a).replace(".", "", 1).isdigit() and '-' in str(arg_b) and str(arg_b).replace("-", "", 1).isdigit():
        return float(arg_a) ** int(arg_b)
    else:
        return 'Invalid value detected!'


def my_func_b(arg_a, arg_b):
    if str(arg_a).replace(".", "", 1).isdigit() and '-' in str(arg_b) and str(arg_b).replace("-", "", 1).isdigit():
        arg_res = arg_a = float(arg_a)
        arg_b = abs(int(arg_b))
        for k in range(1, arg_b):
            arg_res *= arg_a
        return 1 / arg_res
    else:
        return 'Invalid value detected!'


arg_x = (input(f'Введите действительное положительное число x: '))
arg_y = (input(f'Введите целое отрицательное число y: '))
print(f'Result a of x**y: {my_func_a(arg_x, arg_y)}')
print(f'Result b of x^y: {my_func_b(arg_x, arg_y)}')