# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    total = 0
    for letter in text:
        code_letter = ord(letter)
        if code_letter in range(97, 122):
            total += 0
        else:
            total += 1
    if total == 0:
        return text.title()
    else:
        return 'Необходимо использовать маленькие латинские буквы'


print(int_func(input('Введите слово: ')))

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Используйте написанную ранее функцию int_func()

user_list = input('Введите слова через пробел: ')
user_list = user_list.split()
final_list = []
for i in user_list:
    word = int_func(i)
    final_list.append(word)

final_str = ' '.join(final_list)
print(f'Результат - {final_str}')
