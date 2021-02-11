# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

elems_input = []
elems_output = []
list_size = int(input('Введите размер списка: '))
for elem in range(list_size):
	elems_input.append(input(f'Введите элемент №{elem+1}: '))

for elem in range(list_size // 2):
	elem *= 2
	elems_output.extend(reversed(elems_input[elem:elem+2]))
if list_size % 2:
	elems_output.append(int(elems_input[list_size-1]))
for elem in range(list_size):
	print(f'Элемент №{elem+1} = {elems_output[elem]}')

