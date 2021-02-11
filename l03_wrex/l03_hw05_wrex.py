# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

sum_of_typed = 0.0
alt_f4 = False
all_typed_trash = ''
while not alt_f4:
    typed_trash = input(f'Текущая сумма: {sum_of_typed} Введите числа через пробел или Q для выхода:')
    quit_at_index = int(typed_trash.find("Q"))
    if quit_at_index >= 0:
        typed_trash = typed_trash[0:int(quit_at_index)]
        alt_f4 = True
    list_of_trash = ''.join(i for i in typed_trash if i in " 0123456789-.").split()
    print(f'Separated to: {list_of_trash}')  # -----
    for num in list_of_trash:
        try:
            sum_of_typed += float(num)
        except ValueError:
            print(f'Ignored invalid value: {num}')
print(f'Общая сумма: {sum_of_typed}')
