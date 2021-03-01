#  Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
#  который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#  В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
#  уникальные для каждого типа оргтехники.


# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.

def check_list(obj):
    if obj is None:
        obj = list()
        return obj
    else:
        return obj


def check_warehouse():
    if len(Warehouse.all_obj) > 0:
        print('На складе числиться: ')
        for i in Warehouse.all_obj:
            print(i)
        print()
    else:
        print('На складе ни чего нет.')
        print()


def check_division():
    if Warehouse.all_division:
        print('В подразделениях числиться: ')
        for i in Warehouse.all_division:
            for j in Warehouse.all_division[i]:
                print(f'{i}  - {j}')
    else:
        print('В подразделениях нет техники')
    print()


class NotFound(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    all_division = dict()
    all_obj = []

    def __init__(self):
        pass

    @classmethod
    def reception(cls, obj, division):
        try:

            result = cls.all_division.setdefault(division)
            result = check_list(result)
            if (obj not in result) and (obj in cls.all_obj):
                result.append(obj)
                cls.all_division[division] = result
                cls.all_obj.remove(obj)
            else:
                raise NotFound('Данной техники нет на складе')
        except NotFound as err:
            print(err)

    @classmethod
    def transfer(cls, obj):
        try:
            for i in Warehouse.all_division:
                if len(Warehouse.all_division[i]) > 0:
                    for j in Warehouse.all_division[i]:
                        if (j == obj) and (obj not in Warehouse.all_obj):
                            Warehouse.all_division[i].remove(j)
                            Warehouse.all_obj.append(obj)
                        elif obj in cls.all_obj:
                            raise NotFound('Данная техники уже на складе')
        except NotFound as err:
            print(err)


class OfficeEquipment:
    voltage = 220
    color = 'grey'

    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        Warehouse.all_obj.append(self)


class Printer(OfficeEquipment):

    def __init__(self, name, year, price, cartridge='B45', print_speed=120):
        super().__init__(name, year, price)
        self.cartridge = cartridge
        self.print_speed = print_speed

    def __str__(self):
        return f"Принтер {self.name}, год - {self.year}, цена - {self.price}"


class Scanner(OfficeEquipment):

    def __init__(self, name, year, price, mass=30, scanning_speed=200):
        super().__init__(name, year, price)
        self.mass = mass
        self.scanning_speed = scanning_speed

    def __str__(self):
        return f"Сканер {self.name}, год - {self.year}, цена - {self.price}"


class Xerox(OfficeEquipment):

    def __init__(self, name, year, price, lamp='Z-455', copy_speed=50):
        super().__init__(name, year, price)
        self.lamp = lamp
        self.copy_speed = copy_speed

    def __str__(self):
        return f"Ксерокс {self.name}, год - {self.year}, цена - {self.price}"


printer_1 = Printer('LaserJet330-1', 2020, 7000)
printer_2 = Printer('LaserJet330-2', 2021, 7500)

# что на складе
check_warehouse()
# подразделения и что у них на выдаче
check_division()

'''
printer_3 = Printer('LaserJet330-3', 2019, 6500)
scanner_1 = Scanner('LaserPET-1', 2020, 3500)
scanner_2 = Scanner('LaserPET-2', 2019, 3000)
scanner_3 = Scanner('LaserPET-3', 2018, 2000)
xerox_1 = Xerox('Faster-1', 2020, 10000)
xerox_2 = Xerox('Faster-2', 2019, 9000)
xerox_3 = Xerox('Faster-3', 2021, 11000)
'''


Warehouse.reception(printer_1, 'Касса')
Warehouse.reception(printer_2, 'Касса')

# при попытке выдать ошибочно введенный объект приводит к ошибке
Warehouse.reception('sjhdfjhksdkf', 'Касса')

# выдача повторно приводит к ошибке
Warehouse.reception(printer_1, 'Касса')

# что на складе
check_warehouse()
# подразделения и что у них на выдаче
check_division()

# попытка сдать ошибочный объект не проходит
Warehouse.transfer('skjdfhjksd')

Warehouse.transfer(printer_1)

# Повторная сдача техники на склад приводит к ошибке
Warehouse.transfer(printer_1)

# что на складе
check_warehouse()
# подразделения и что у них на выдаче
check_division()
