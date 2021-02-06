# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_2_var(dividend, divider):
    try:
        result = dividend / divider
        return result
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


while True:
    dividend = input('Ведите делимое: ')
    divider = input('Введите делитель: ')
    if divider.isdigit() and dividend.isdigit():
        dividend = int(dividend)
        divider = int(divider)
        break
    print("Необходимо ввести числа")

result = division_2_var(dividend, divider)
print(result)
