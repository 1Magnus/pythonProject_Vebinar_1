# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
def ischeck_number(a):
    try:
        float(a)
        return True
    except TypeError:
        False


finish_list = []
number_employees = 0
all_salary = 0
with open('text_3.txt', encoding='utf-8') as f:
    for str_f in f:
        number_employees += 1
        str_f = str_f.split()
        salary = float(str_f[1])
        all_salary += salary
        if salary < 20000:
            finish_list.append(str_f[0])

average_salary = all_salary / number_employees

print(f'Список сотрудников с зарплатой менее 20 тыс.: {finish_list} ')
print(f'Среднея величина дохода на сотрудника - {average_salary}')