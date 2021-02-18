# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка

with open('text.txt', 'w', encoding='utf-8') as f:
    user_text = 1
    while not user_text == "":
        user_text = input('Введите текст: ')
        f.writelines(f'{user_text} \n')
