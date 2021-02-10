# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce


def multiplication_dat(s_1, s_2):
    return s_1 * s_2


new_list = [el for el in range(99, 1001) if el % 2 == 0]
print(new_list)
result = reduce(multiplication_dat, new_list)
print(f'Результат = {result}')
