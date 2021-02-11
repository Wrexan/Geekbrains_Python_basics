# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

import time


class NUL_DIVISION(Exception):
    @staticmethod
    def err():
        print("Всё ок, вы поделили на ноль.")
        time.sleep(1)
        print("Для точного подсчета потребуется немного вечности.")
        time.sleep(3)
        print("Ваше железо не справляется. Хотите продолжить деление?")


something = " "
while something != "666":
    something = input("Делим 10 на: ")
    try:
        if int(something) == 0:
            raise NUL_DIVISION
        print(f'Вышло: {10 / int(something)}')
    except NUL_DIVISION as n:
        n.err()
    except:
        print(f'Вы ввели {something}. Пожалуйста, опрерируйте целыми числами. Для выхода: 666')
print(f'Вышло: на совсем')