# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

str_in = input("Type a big number:")
str_len = len(str_in)
str_biggest_num = str_in[0]
i = 1
while i < str_len:
    if str_in[i] > str_biggest_num:
        str_biggest_num = str_in[i]
    i += 1
print(f"Biggest digital is: {str_biggest_num}")