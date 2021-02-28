# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите делимое и делитель через пробел: ")

try:
    result = list(map(int, inp_data.split()))
    if result[1] == 0:
        raise MyException('На ноль делить нельзя')
except ValueError:
    print("Вы ввели не числа")
except MyException as err:
    print(err)
else:
    print(f"Результат =  {result[0] / result[1]}")


