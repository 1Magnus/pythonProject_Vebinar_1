# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import time


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Data:

    def __init__(self, data_str):
        try:
            if (type(data_str) is str) and (data_str.count('-') == 2):
                self.data_str = data_str
            else:
                raise MyException('Необходимо ввести строку в формате: «день-месяц-год»')
        except MyException as err:
            print(err)

    @classmethod
    def extracts_number(cls, param):
        f_result = list(map(int, param.split('-')))
        return f_result

    @staticmethod
    def date_check(date):
        try:
            time.strptime(date, '%d-%m-%Y')
            return 'Дата верна'
        except ValueError:
            return 'Неверная дата'


data_1 = Data('28-02-2021')
data_2 = Data(29022020)
print(data_1.extracts_number(data_1.data_str))
print(data_1.date_check(data_1.data_str))

print(Data.extracts_number('28-02-2021'))
print(Data.date_check('28-02-2021'))
print(Data.date_check('31-02-2021'))
print(Data.date_check('11-13-2021'))
print(Data.date_check('28-02-22222'))

