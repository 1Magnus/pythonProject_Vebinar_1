# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict

# while True:
manth = input("Введите месяц от 1 до 12: ")
#  if manth.isdigit():
#      manth = int(manth)
#      if manth < 13 and manth > 0:
#          break
#  print("Необходимо ввести число от 1 до 12")

winter = ['12', '1', '2']
spring = ['3', '4', '5']
summer = ['6', '7', '8']
autumn = ['9', '10', '11']

if manth in winter:
    print('Зима - list')
elif manth in spring:
    print('Весна - list')
elif manth in summer:
    print('Лето - list')
elif manth in autumn:
    print('Осень - list')
else:
    print('Необходимо ввеси число от 1 до 12')
my_dict = {'12': 'Зима', '1': 'Зима', '2': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето', '7': 'Лето',
           '8': 'Лето', '9': 'Осень', '10': 'Осень', '11': 'Осень'}
if manth in my_dict:
    print(f'{my_dict[manth]} - dict')
else:
    print('Необходимо ввеси число от 1 до 12')
