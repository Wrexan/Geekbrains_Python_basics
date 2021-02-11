# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict

seasons = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
month_found = False

month_num_in = int(input('Type a number of month: '))
for season in seasons:
    for month in seasons.get(season):
        if month == month_num_in:
            print(f'Month {month} is {season}')
            month_found = True
            break
if not month_found:
    print(f'There is no season for month with number {month_num_in}')
