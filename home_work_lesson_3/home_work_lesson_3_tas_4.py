# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла
def my_func(x, y):
    x = float(x)
    y = abs(int(y))
    result = 1 / (x ** y)
    return result


def my_fanc_ver_2(x, y):
    x = float(x)
    y = abs(int(y))
    result = 1
    for i in range(y):
        result = result * 1 / x
    return result


def check_negative(y):
    try:
        y = int(y)
        if (y < 0):
            return True
        return False
    except ValueError:
        return False


def check_number(x):
    try:
        x = float(x)
        if (x >= 0):
            return True
        return False
    except ValueError:
        return False


x = input('Укажите X: ')
while not check_number(x):
    print('Необходимо ввести положительно число')
    x = input('X: ')

y = input('Укажите Y:')
while not check_negative(y):
    print('Необходимо ввести отрицательное цисло')
    y = input('Y: ')

result = my_func(x, y)
print(f'Результат = {result}')

result = my_fanc_ver_2(x, y)
print(f'Результат = {result} - 2 Вариант')
