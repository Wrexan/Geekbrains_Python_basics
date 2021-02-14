# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NOT_A_NUMBER(Exception):
    @staticmethod
    def is_number(string):
        return True if string and (string[0] == "-" and string.replace("-", "", 1).replace(".", "", 1).isdigit()
                                   or string.replace(".", "", 1).isdigit()) else False


something = ""
collector = []
while something != "stop":
    something = input("Введите число: ")
    try:
        if NOT_A_NUMBER.is_number(something):
            collector.append(something)
        else:
            raise NOT_A_NUMBER
    except NOT_A_NUMBER as n:
        print(f'Не добавлено: {something}')
print(f'Вышло: {collector}')
