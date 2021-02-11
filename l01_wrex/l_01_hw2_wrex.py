# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк

seconds_in = int(input("Type any time in seconds:"))

hours_hh = seconds_in // 3600
minutes_mm = seconds_in // 60 - hours_hh * 60
seconds_ss = seconds_in % 60

if seconds_ss <= 0:
    seconds_ss = "00"
elif seconds_ss <= 9:
    seconds_ss = "0" + str(seconds_ss)
if minutes_mm <= 0:
    minutes_mm = "00"
elif minutes_mm <= 9:
    minutes_mm = "0" + str(minutes_mm)

print(f"{hours_hh}:{minutes_mm}:{seconds_ss}")
