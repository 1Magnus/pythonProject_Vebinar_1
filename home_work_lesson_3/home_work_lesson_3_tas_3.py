# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(arg1, arg2, arg3):
    list_arg = [arg1, arg2, arg3]
    result = sum(list_arg) - min(list_arg)
    return result


while True:
    number1 = input('Введите первое число: ')
    number2 = input('Введите второе число: ')
    number3 = input('Введите третье число: ')
    if number1.isdigit() and number2.isdigit() and number3:
        number1 = int(number1)
        number2 = int(number2)
        number3 = int(number3)
        break
    print("Необходимо ввести числа")
result = my_func(number1, number2, number3)
print(f'Сумма двух наибольших чисел = {result}')
