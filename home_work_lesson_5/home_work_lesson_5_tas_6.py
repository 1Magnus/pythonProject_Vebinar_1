# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
def find_number(el_str):
    if not el_str.isdigit():
        for i, char in enumerate(el_str):
            if not char.isdigit():
                return el_str[:i]
    else:
        return el_str


result_dict = {}
number_clock = []

with open('text_6.txt', encoding='utf-8') as f:
    for str_f in f:
        first = str_f.index(':')
        subject = str_f[:first]
        two_pass = str_f[first:]
        two_pass = two_pass.split()

        for el in two_pass:
            if el[:1].isdigit():
                number = find_number(el)
                number = int(number)
                number_clock.append(number)
                result_dict[subject] = sum(number_clock)
        number_clock = []

print(result_dict)
