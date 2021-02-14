# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

all_profit = 0
all_firm_finish = 0
finish_dict = {}
finish_dict_2 = {}
finish_list = []
with open('text_7.txt', encoding='utf-8') as f:
    for str_f in f:
        str_f = str_f.split()
        profit = int(str_f[2]) - int(str_f[3])
        finish_dict[str_f[0]] = profit
        if profit > 0:
            all_profit += profit
            all_firm_finish += 1

average_profit = all_profit / all_firm_finish
finish_dict_2['average_profit'] = average_profit

finish_list.append(finish_dict)
finish_list.append(finish_dict_2)
print(finish_list)

with open('text_7.json', 'w', encoding='utf-8') as f_2:
    json.dump(finish_list, f_2, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))

