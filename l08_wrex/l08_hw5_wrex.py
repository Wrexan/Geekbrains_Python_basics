# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 0: {'units': 1, 'type': 'printer', 'manuf': 'Samsung', 'model': 'M1200b', 'color': 'black', 'cost': 8100,
# 'assign': STOCK},
class OEStock:
    stock = {1: ('6', 'STOCK', 'printer', 'Samsung', 'M1200b', 'black', '4100', 'True'),
             6: ('2', 'PRDEP', 'printer', 'Samsung', 'M1200w', 'white', '4050', 'True'),
             15: ('13', 'PROD', 'printer', 'Epson', 'X300+', 'black', '6390', 'False'),
             2: ('2', 'PRDEP', 'copier', 'Xerox', 'XC1522', 'grey', '12450', 'True', '20', '10')}

    controls = [['отобразить', 'поиск', 'добавить', 'удалить', 'переместить', 'сохранить', 'выход'],
                ['1', '2', '3', '4', '5', '6', '0']]

    params = ['id', 'units', 'assign']

    data_file = "l05_hw7_text.pdb"

    def __init__(self, inv):
        self.inv = inv
        self.menu_len = len(self.inv.fields) + len(self.params)
        working = 1
        self.load()
        while working:
            print(self.c1(" ".join(self.controls[1][i] + ")" + self.controls[0][i] for i in
                                   range(len(self.controls[0])))))
            command = input(self.c1('Введите действие: '))
            if command == '1':
                self.show_all()
            elif command == '2':
                self.show_all(input(self.c1('Введите искомое поле: ')))
            elif command == '3':
                adding_1 = tuple(input(f"{self.c1('Введите поля через запятую: ')}"
                                       f"{self.c4([self.params[1]] + self.inv.fields)}\n"
                                       f"{self.c1('Доступные типы: ')} {self.c4(self.inv.types)}\n"
                                       f"").strip().split(','))
                if len(adding_1) == len(self.inv.fields) + 1 and int(adding_1[0]) > 0:
                    if adding_1[1] == self.inv.types[0]:
                        self.income(adding_1, Printer.fields)
                    elif adding_1[1] == self.inv.types[1]:
                        self.income(adding_1, Scanner.fields)
                    elif adding_1[1] == self.inv.types[2]:
                        self.income(adding_1, Copier.fields)
                    else:
                        print(self.c3('Неверный тип техники! Доступно: ' + str(self.inv.types)))
                else:
                    print(self.c3(f'Неверное кол-во полей (Доступно: {len(self.inv.fields) + 1})'
                                  f' или неверное кол-во единиц техники! {adding_1[0]}'))

            elif command == '4':
                self.show_all()
                self.outcome(input(self.c1('Для удаления ведите: ' + self.c4('ID, количество: '))), 0)
            elif command == '5':
                self.show_all()
                self.outcome(input(self.c1('Для перемещения ведите: ' + self.c4('ID, количество: '))), 1)
            elif command == '6':
                self.save()
            elif command == '0':
                working = 0
                print(self.c4('Спасибо, что возпользовались нашим продуктом. До встречи!'))

    def show_all(self, key=''):
        text = ''
        le = self.menu_len - 1
        if key != '':
            if key in self.inv.types:
                text = '\t\t' + '\t\t'.join(Printer.fields) if key == self.inv.types[0] else \
                    '\t\t'.join(Scanner.fields) if key == self.inv.types[1] else \
                    '\t\t'.join(Copier.fields)
                le = 20

        print(self.c2(self.params[0] + '\t' + self.params[1] + '\t' + self.params[2] + '\t\t' + '\t\t'.join(
            self.inv.fields) + text))
        for b in self.stock:
            pos = self.stock.get(b)
            if key:
                if key == str(b) or key in pos:
                    if pos[1] == 'STOCK':
                        print(str(b) + '\t' + '\t\t'.join(pos[:le]))
                    else:
                        print(self.c5(str(b) + '\t' + '\t\t'.join(pos[:le])))
            else:
                if pos[1] == 'STOCK':
                    print(str(b) + '\t' + '\t\t'.join(pos[:le]))
                else:
                    print(self.c5(str(b) + '\t' + '\t\t'.join(pos[:le])))

    def income(self, adding_1, fields):
        adding_2 = tuple(input(self.c1('Введите поля через запятую: ') + self.c4(
            fields)).split(','))
        if len(adding_2) == len(fields):
            print(adding_1[0:1] + ('STOCK',) + adding_1[1:], adding_2)
            self.pos_adder(adding_1[0:1] + ('STOCK',) + adding_1[1:], adding_2)
            return
        else:
            print(self.c3('Неверное кол-во полей!'))

    def pos_adder(self, params_1, params_2):
        p = params_1 + params_2
        for k in self.stock:  # add element to the old, if exist
            if p[1:] == self.stock.get(k)[1:]:
                self.stock.update({k: (str(int(p[0]) + int(self.stock.get(k)[0])),) + p[1:]})
                print(self.c3('Добавлено к существующей позиции: ') + self.c4(str({k: p})))
                return
        for i in range(1, 10000):  # add element with new id
            if i not in self.stock:
                self.stock.update({i: p})
                print(self.c3('Добавлена новая позиция: ') + self.c4(str({i: p})))
                return

    def outcome(self, key, do_edit):
        t = list(key.strip().split(','))
        if t[0] and (len(t) == 1 or len(t) == 2):
            pos_id = t[0].strip()
            pos_units = '1' if len(t) == 1 else t[1].strip()
        else:
            print(self.c3('Неверное количество данных! Введите: '
                          '' + self.c4('ID') + self.c3(' или ') + self.c4('ID, Коли-во')))
            return
        try:
            pos_id = int(pos_id.strip())
            pos_units = int(pos_units.strip())
        except ValueError:
            print(self.c3('Неверные данные! Кол-во и ID - натуральные числа выше 0'))
            return
        if pos_id <= 0 or pos_units <= 0:
            print(self.c3('Неверные данные! Кол-во и ID - натуральные числа выше 0'))
            return
        if pos_id in self.stock:
            print(self.c2(self.params[0] + '\t' + self.params[1] + '\t' + self.params[2] + '\t\t' + '\t\t'.join(
                self.inv.fields)))
            pos = self.stock.get(pos_id)
            print(str(pos_id) + '\t' + '\t\t'.join(pos[:self.menu_len - 1]))
            p_have = int(pos[0])
            if p_have < pos_units:
                pos_units = p_have
            if do_edit:
                yn = input(self.c3(f'Введите {self.c4("код отдела")} {self.c3("для перемещения или")}'
                                   f' {self.c4("ничего")} {self.c3("для отмены")} {pos_units} шт. ')).strip()[
                     :5].upper()
                if yn:
                    old_pos = self.stock.pop(pos_id)
                    if p_have > pos_units:
                        self.stock.update({pos_id: (str(p_have - pos_units),) + tuple(old_pos)[1:]})
                        self.pos_adder((str(pos_units),) + tuple(old_pos)[0:0] + (yn,), tuple(old_pos)[2:])
                    else:
                        self.pos_adder((str(pos_units),) + tuple(old_pos)[0:0] + (yn,), tuple(old_pos)[2:])
                    self.show_all()
                return
            else:
                yn = input(self.c3(f'Подтвердите удаление {pos_units} шт. {self.c4("(y)")} '))
            if yn == 'y':
                if p_have > pos_units:
                    self.stock.update({pos_id: (str(p_have - pos_units),) + tuple(self.stock.pop(pos_id))[1:]})
                else:
                    self.stock.pop(pos_id)
                self.show_all()
                return
            else:
                return
        else:
            print(self.c3('Не найден ID ' + self.c4(pos_id)))

    @staticmethod  # Green - menu
    def c1(text):
        return f'\033[1;32;32m{text}\033[0m'

    @staticmethod  # B/W
    def c2(text):
        return f'\033[1;30;47m{text}\033[0m'

    @staticmethod  # Yellow - attention
    def c3(text):
        return f'\033[1;32;33m{text}\033[0m'

    @staticmethod  # Blue - example
    def c4(text):
        return f'\033[1;32;34m{text}\033[0m'

    @staticmethod  # Grayish - example
    def c5(text):
        return f'\033[2;30;37m{text}\033[0m'

    @classmethod
    def save(cls):
        try:
            with open(cls.data_file, "w", encoding="utf-8") as w:
                w.write(str(cls.stock))
        except IOError:
            print(f"{cls.c3('Не удается сохранить файл: ')}{cls.data_file}")
        else:
            print(f"{cls.c4('База успешно сохранена в файл: ')}{cls.data_file}")

    @classmethod
    def load(cls):
        try:
            with open(cls.data_file, "r", encoding="utf-8") as r:
                cls.stock = eval(r.read())
                print(cls.stock)
        except IOError:
            print(f"{cls.c3('Не удается загрузить файл: ')}{cls.data_file}")
        else:
            print(f"{cls.c4('База успешно загружена из: ')}{cls.data_file}")


class OfficeEquipment:
    types = ['printer', 'scanner', 'copier']
    fields = ['type', 'made by', 'model', 'color', 'cost']
    id = 0
    type = 'None'
    manuf = 'None'
    model = 'None'
    color = 'None'
    cost = 0


class Printer(OfficeEquipment):
    fields = ['is_laser']

    def __init__(self, is_laser=True):
        self.is_laser = is_laser


class Scanner(OfficeEquipment):
    fields = ['size', 'speed']

    def __init__(self, work_size=20, speed=0):
        self.work_size = work_size
        self.speed = speed


class Copier(OfficeEquipment):
    fields = ['auto', 'size', 'speed']

    def __init__(self, auto='True', work_size=20, speed=0):
        self.work_size = work_size
        self.speed = speed
        self.auto = auto


MyStock = OEStock(OfficeEquipment)
