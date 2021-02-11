# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide_ab(c, d):
    if c.replace(".", "", 1).isdigit() and d.replace(".", "", 1).isdigit() and int(d) != 0:
        return float(c) / float(d)
    else:
        return "Error. Unaccepted arguments!"


a = input('Enter a: ')
b = input('Enter b: ')
print(divide_ab(a, b))
