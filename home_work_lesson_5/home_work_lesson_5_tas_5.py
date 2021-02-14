# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
import random

n = 10
with open('text_5.txt', 'a', encoding='utf-8') as f_2:
    number = [random.randint(1, 100) for el in range(5)]
    for i in number:
        print(i, file=f_2, end=' ')

finish_list = []
with open('text_5.txt', encoding='utf-8') as f:
    f_str = f.read()
    f_list = f_str.split()
    for i in f_list:
        i = int(i)
        finish_list.append(i)
    result = sum(finish_list)
print(f'Сумма чисел в файле равна = {result}')

