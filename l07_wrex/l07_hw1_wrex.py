# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации
# операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        matrix_p = '\n'.join(str(i) for i in self.matrix_list)
        return f'{matrix_p}'

    def __add__(self, other):
        new_matrix = []
        matrix_size = min(len(self.matrix_list), len(other.matrix_list))
        for i in range(matrix_size):
            new_line = []
            for j in range(matrix_size):
                new_line.append(self.matrix_list[i][j] + other.matrix_list[i][j])
            new_matrix.append(new_line)
        return Matrix(new_matrix)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 5, 4], [2, 0, 5], [2, 1, 8]])

print(f'{m1}\n')
print(f'{m2}\n')

m3 = m1 + m2
print(f'{m3}\n')

