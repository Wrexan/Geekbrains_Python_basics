# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__())
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, cells):
        try:
            self.cells = int(cells)
        except ValueError:
            print(f'ERROR! Illegal value in Cell.cells: {self}.cells = {self.cells}')

    def __add__(self, other):
        if isinstance(other, Cell):
            cells = self.cells + other.cells
        else:
            print(f'ERROR! Illegal second value in method Cell.__add__ {type(other)} = {other}')
            cells = 0
        return Cell(cells)

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.cells >= other.cells:
                cells = self.cells - other.cells
            else:
                cells = 0
                print(f'Warning! bigger value {other}.cells = {other.cells} '
                      f'subtracting from lesser {self}.cells = {self.cells}')
        else:
            print(f'ERROR! Illegal second value in method Cell.__sub__ {type(other)} = {other}')
            cells = 0
        return Cell(cells)

    def __mul__(self, other):
        if isinstance(other, Cell):
            cells = self.cells * other.cells
        else:
            print(f'ERROR! Illegal second value in method Cell.__mul__ {type(other)} = {other}')
            cells = 0
        return Cell(cells)

    def __truediv__(self, other):
        if isinstance(other, Cell):
            try:
                cells = int(self.cells / other.cells)
                if cells <= 0:
                    print(f'Warning! negative value {self}.cells = {self.cells} '
                          f'divided by {other}.cells = {other.cells}')
                    cells = 0
            except ZeroDivisionError:
                cells = 0
                print(f'Warning! zero division {other}.cells = {other.cells} '
                      f'divided by zero {self}.cells = {self.cells}')
        else:
            print(f'ERROR! Illegal second value in method Cell.__truediv__ {type(other)} = {other}')
            cells = 0
        return Cell(cells)

    def make_order(self, size):
        string = ''
        for i in range(self.cells):
            if not (i % size):
                if i > 0: string += '\n'
            string += '*'
        return string


cell_1 = Cell(51)
cell_2 = Cell(3)
print(f'cell_1 = {cell_1.cells} | cell_2 = {cell_2.cells}')
print(cell_1.make_order(10))
print(cell_2.make_order(10))

cell_3 = cell_1 + cell_2
print(f'(__add__) = {cell_3.cells}')
print(cell_3.make_order(10))

cell_4 = cell_1 - cell_2
print(f'(__sub__) = {cell_4.cells}')
print(cell_4.make_order(10))

cell_5 = cell_1 * cell_2
print(f'(__mul__) = {cell_5.cells}')
print(cell_5.make_order(10))

cell_6 = cell_1 / cell_2
print(f'(__truediv__) = {cell_6.cells}')
print(cell_6.make_order(10))


