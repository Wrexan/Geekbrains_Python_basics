# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    dd_mm_yy = "01-01-0000"

    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = self.is_date_ok(dd_mm_yy)
        print(f'{dd_mm_yy} {Date.is_date_ok(dd_mm_yy)}')

    @classmethod
    def digitize_date(cls, date):
        ddmmyy = date.split("-")
        return ddmmyy

    @staticmethod
    def is_date_ok(date_str_or_list):
        ddmmyy = list(map(int, Date.digitize_date(date_str_or_list))) if type(date_str_or_list) == str else \
            list(map(int, date_str_or_list))
        big_months = [1, 3, 5, 7, 8, 10, 12]
        is_leap = 1 if ddmmyy[2] % 400 == 0 or (ddmmyy[2] % 4 == 0 and ddmmyy[2] % 100 != 0) else 0
        if 0 <= int(ddmmyy[2]) <= 9999 and 1 <= int(ddmmyy[1]) <= 12:
            if 1 <= int(ddmmyy[0]) <= (28 + is_leap if ddmmyy[1] == 2 else 31 if ddmmyy[1] in big_months else 30):
                return True
        return False


# Work of methods
date_from_class_method = Date.digitize_date('21-12-1234')
print(date_from_class_method)
print(Date.is_date_ok(date_from_class_method))

# Work through the Object
date_from_object = Date('12-34-5678')

# Functionality
print(f"11-02-2021 {Date.is_date_ok('11-02-2021')}")
print(f"11-02-12021 {Date.is_date_ok('11-02-12021')}")
print(f"11-29-2021 {Date.is_date_ok('11-29-2021')}")
print(f"29-02-2020 {Date.is_date_ok('29-02-2020')}")
print(f"29-02-2021 {Date.is_date_ok('29-02-2021')}")
print(f"29-02-2021 {Date.is_date_ok('29-02-2021')}")
print(f"31-03-2021 {Date.is_date_ok('31-03-2021')}")
print(f"31-04-2021 {Date.is_date_ok('31-04-2021')}")

