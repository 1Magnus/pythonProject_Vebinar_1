# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_list = input('Введите слова через пробел: ')
user_list = user_list.split()
print(f'Ваш список: {user_list}')
my_list = []

for i in user_list:
    if len(i) > 10:
        i = i[:10]
    my_list.append(i)

for i in enumerate(my_list, 1):
    print(i)
