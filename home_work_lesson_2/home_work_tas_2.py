# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


while True:
    length_user = input('Укажите длину списка: ')
    if length_user.isdigit():
        length_user = int(length_user)
        break
    print("Необходимо ввести число")

my_list = []

for i in range(length_user):
    element = input('Введите элемент списка: ')
    my_list.append(element)

print(f'Ваш список: {my_list}')

for k in range(length_user):
    if k % 2 == 0:
        my_list[k] = my_list[k - 1]


print(f'Новый список: {my_list}')


