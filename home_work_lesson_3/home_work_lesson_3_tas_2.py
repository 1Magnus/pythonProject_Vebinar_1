# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой

def personal_information(**kwargs):
    return kwargs


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
telephone = input('Введите номер телефона: ')

dict_pers_inf = personal_information(name=name, surname=surname, year_of_birth=age, city=city, email=email,
                                     telephone=telephone)

print(dict_pers_inf)

