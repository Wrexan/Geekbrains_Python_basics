# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

a_few_words_str = input('Type a few words with spaces: ')
a_few_words_lst = []
i = 1
for word in a_few_words_str.split(" "):
    if len(word) > 10:
        word = word[:10]
    print(f'{i}) {word}')
    i += 1
