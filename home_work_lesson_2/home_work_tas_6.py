# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.

all_list = []
characteristics_dicts = []
# Так как в задании написано чет все данные заправшиваем у пользователя, значение ключей вводиться тоже с клавиатуры
quantity = int(input('Программа "Товары", для заполнения используйте пример \n'
                     '"название компьютер цена 20000 количество 5 eд шт." \n'
                     'Укажите количество товаров: '))
for i in range(quantity):
    user_answer = input('Введите характериситики товара через пробел: ')
    my_list = user_answer.split()
    my_dict = dict(zip(my_list[::2], my_list[1::2]))
    characteristics_dicts.append(my_dict)

print('*' * 150)

for i in enumerate(characteristics_dicts, 1):
    all_list.append(i)
print(all_list)

print('*' * 150)

analitic_dict = {}
characters_in_mas = []
all_key = my_dict.keys()
for key in all_key:
    for mas in characteristics_dicts:
        character_in_mas = mas.get(key)
        characters_in_mas.append(character_in_mas)

    analitic_dict[key] = characters_in_mas
    characters_in_mas = []
print(analitic_dict)
