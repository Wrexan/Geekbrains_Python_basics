# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, a, b):
        if This.is_number(str(a)) and This.is_number(str(b)):
            self.a = float(a)
            self.b = float(b)
        else:
            self.a = 0
            self.b = 0
            print(f'ERROR! Expected numbers in a or b. Got: {self}.a = {a}, {self}.a = {a}')

    def __str__(self):
        return f'{round(self.a, 2)}+{round(self.b, 2)}i'

    def __add__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.a + other.a, self.b + other.b)
        else:
            print(f'ERROR! Illegal second value in method ComplexNum.__add__ {type(other)} = {other}')

    def __mul__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum((self.a * other.a) - (self.b * other.b), (self.b * other.a) + (self.a * other.b))
        else:
            print(f'ERROR! Illegal second value in method ComplexNum.__mul__ {type(other)} = {other}')


class This:
    @staticmethod
    def is_number(string: str):
        return True if string and (
                string[0] == "-"
                and string.replace("-", "", 1).replace(".", "", 1).isdigit()
                or string.replace(".", "", 1).isdigit()) else False


alpha = ComplexNum(-2, 5.15)
beta = ComplexNum(3.666, 20)

kappa = alpha + beta
print(f'kappa({alpha} + {beta}) = {kappa}')
omega = alpha * beta
print(f'omega({alpha} * {beta}) = {omega}')
