# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой

def personal_information(**kwargs):
    return kwargs


def personal_inf_vers_2(**kwargs):
    pers_inf_list = list(kwargs.values())
    print(f'Имя: {pers_inf_list[0]}, Фамилия: {pers_inf_list[1]}, Год рождения: {pers_inf_list[2]}, '
          f'Город проживания: {pers_inf_list[3]}, Email: {pers_inf_list[4]}, Телефон: {pers_inf_list[5]} - '
          f'Вывод уже в функции')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
telephone = input('Введите номер телефона: ')

dict_pers_inf = personal_information(name=name, surname=surname, year_of_birth=age, city=city, email=email,
                                     telephone=telephone)
# Просто выводит словарь в одну строку
print(dict_pers_inf)
# Вывод № 2
pers_inf_val = list(dict_pers_inf.values())
print(f'Имя: {pers_inf_val[0]}, Фамилия: {pers_inf_val[1]}, Год рождения: {pers_inf_val[2]}, '
      f'Город проживания: {pers_inf_val[3]}, Email: {pers_inf_val[4]}, Телефон: {pers_inf_val[5]}')

# Вывод № 3 уже из функции
personal_inf_vers_2(name=name, surname=surname, year_of_birth=age, city=city, email=email,
                    telephone=telephone)
