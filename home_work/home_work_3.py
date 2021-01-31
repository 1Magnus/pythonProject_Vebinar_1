# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
n = input('Введите число n  ')

n2 = n + n
n3 = n + n + n

result = int(n) + int(n2) + int(n3)
print(f'Сумма: {n} + {n2} + {n3} = {result}')
