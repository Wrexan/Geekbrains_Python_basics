# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

line, low_salary_num = " ", 20000
mess = ["Следующие сотрудники получают менее ", "Средняя зарплата: ", " гривен", "--Не удается прочесть файл: ",
        "--Не удается обработать зарплату: "]
employee_data_file = "l05_hw3_text.txt"
num_of_employees = sum_of_salary = eof = 0
try:
    with open(employee_data_file, "r", encoding="utf-8") as f:
        print(f"{mess[0]}{low_salary_num}{mess[2]}")
        while not eof:
            line = f.readline()
            if line:
                params = line.split()
                try:
                    zp = int(params[1])
                    sum_of_salary += zp
                    num_of_employees += 1
                    if zp < low_salary_num:
                        print(params[0])
                except (ValueError, IndexError):
                    print(f"{mess[4]}{params}")
            else:
                eof = 1
    print(f"{mess[1]}{round(sum_of_salary / num_of_employees, 2)}{mess[2]}")
except IOError:
    print(f"{mess}{employee_data_file}")
