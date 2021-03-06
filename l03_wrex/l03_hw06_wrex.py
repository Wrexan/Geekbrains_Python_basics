# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# ============================================== SIMPLE =============================================
# def int_func(text='No text'):
#     return text.lower().capitalize()
#
#
# print(f"{' '.join(i for i in map(int_func, input('Type a few words with space: ').split()))}")

# ============================================== ord() =============================================
def int_func(text='No text'):
    char = ord(text[0])
    return chr(char - 32) + text[1:] if char in range(97, 123) else text


print(f"{' '.join(i for i in map(int_func, input('Type a few words with space: ').split()))}")
