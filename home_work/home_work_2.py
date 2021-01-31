# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# import time

sec_numb = int(input('Введите время в секундах:  '))
# функция добавлена для проверки
# print(time.strftime('%H:%M:%S', time.gmtime(sec_numb)))

hours = 00
seconds = sec_numb % 60
sec_numb = sec_numb - seconds
mints = (sec_numb // 60) % 60
hours = (sec_numb // 3600) % 24

print(f'Результат:  {hours}:{mints}:{seconds}')
