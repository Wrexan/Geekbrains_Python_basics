# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в
# переменные, затем выведите на экран.
# tell me about your cat a little

cat_name = input("Tell me your cat's name:")
cat_age = int(input("Your cat's age?:"))
cat_color = input("What color is it have?:")
cat_tail = int(input(f"How many {cat_color} tails it have to pull?:"))
cat_mass = float(input(f"And a weight of your {cat_name}?:"))

by_tail = ""
letter_s = ""
if cat_tail > 0:
    by_tail = f" by the {cat_tail} {cat_color} tail"
    if cat_tail > 1:
        letter_s = "s"

print(f"So. Your {cat_name} had {cat_age} years to grow to {cat_mass} kg, and now we can't lift it{by_tail}{letter_s}?")

