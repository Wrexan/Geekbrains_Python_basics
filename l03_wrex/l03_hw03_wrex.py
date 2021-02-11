# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_a, arg_b, arg_c):
    try:
        arg_a = float(arg_a)
        arg_b = float(arg_b)
        arg_c = float(arg_c)
    except ValueError:
        return 'Invalid value detected!'
    return (arg_a + arg_b + arg_c) - min(arg_a, arg_b, arg_c)


args = []
for i in range(3):
    args.append(input(f'Type argument {i+1}: '))
print(f'Result: {my_func(args[0], args[1], args[2])}')
