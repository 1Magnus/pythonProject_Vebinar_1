# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.


my_list = [7, 5, 3, 3, 2]
print(f'Исходный список Рейтинга: {my_list}')
# Решение через Sort.
# number = True
# while number:
#  number = int(input('Введите новый элемент рейтинга: '))
#  copy_list = my_list.copy()
# copy_list.append(number)
# copy_list.sort(reverse=True)
# print(f'Результат - {copy_list} Для окончания работы введите 0')

while True:
    number = input("Введите новый элемент рейтинга: ")
    if number.isdigit():
        number = int(number)
        break
    print("Необходимо ввести положительно число")

chek = True
for i in range(len(my_list)):
    if number > my_list[i]:
        my_list.insert(i, number)
        chek = False
        break
if chek:
    my_list.append(number)

print(f'Результат - {my_list}')
