# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

entered_text: str = " "

try:
    with open("l05_hw1_text.txt", "w") as f:
        while not entered_text == "":
            entered_text = input("Введите текст: ")
            f.write(f'{entered_text}\n')
except:
    print(f"--Can't create/open file 'l05_wh1_text'")
