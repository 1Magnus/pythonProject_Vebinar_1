# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке

with open('text.txt', encoding='utf-8') as f:
    number_str = 0
    number_swar = []
    for str_f in f:
        number_str += 1
        number_swar.append(str_f.count(' ') + 1)

print(f'Количество строк: {number_str}.')
for i in enumerate(number_swar, 1):
    print(f'Количество слов в строке № {i[0]} - {i[1]}')

