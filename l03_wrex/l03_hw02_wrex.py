# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# check year for digits, email for @, tel for digits
def print_dossier(name, sr_name, yr_of_birth, lvng_place, email, tel):
    if str(yr_of_birth).isdigit() and '@' in email and \
            tel.replace("+", "", 1).replace("-", "", 4).replace(" ", "", 4).isdigit():
        print(f'Subject: {sr_name} {name}, born in {yr_of_birth}. '
              f'Place of residence: {lvng_place}. Email {email}, tel: {tel}')


print_dossier(tel='+380 44-123-45-67', email='ja_pozyril@po4ty.net',
              yr_of_birth=2020, name='Uasa', sr_name='Pupkin', lvng_place='Zabobruevo')
