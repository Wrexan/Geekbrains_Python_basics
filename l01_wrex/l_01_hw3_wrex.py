# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

entered_num = int(input("Type random number"))
if entered_num <= 9:
    mn11 = 11
    mn111 = 111
elif entered_num <= 99:
    mn11 = 101
    mn111 = 10101
else:
    mn11 = 1001
    mn111 = 1001001

print(f"{entered_num * mn111  + entered_num * mn11 + entered_num}")