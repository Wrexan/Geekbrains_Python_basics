# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
stock = []
units = ('шт.', 'кг', 'л')
stock_names = []
stock_prices = []
stock_amounts = []
stock_units = []

item_types = int(input('Сколько видов товаров вы хотите ввести: '))
for i in range(item_types):
    item_name = input(f'Название товара №{i+1}: ')
    item_price = int(input(f'Цена товара "{item_name}" №{i+1}: '))
    item_units = int(input(f'Единицы измерения 1 = {units[0]}, 2 = {units[1]}, 3 = {units[2]}: ')) - 1
    item_amount = int(input(f'Количество {units[item_units]}: '))
    stock.append((i+1, {'название': item_name, "цена": item_price, 'количество': item_amount, "ед": units[item_units]}))

for k in range(len(stock)):
    stock_names.append(stock[k][1]['название'])
    stock_prices.append(stock[k][1]['цена'])
    stock_amounts.append(stock[k][1]['количество'])
    stock_units.append(stock[k][1]['ед'])

stock_sorted = {'название': stock_names, 'цена': stock_prices, 'количество': stock_amounts, 'ед': stock_units}
print(stock_sorted, "\n")

# stock_a = {'название': item_name, "цена": item_price, 'количество': item_amount, "ед": item_units}
