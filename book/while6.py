from random import randint, uniform
import math
# print(f'd = {d}')
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
d = randint(0, 100)
e = randint(0, 100)
f = randint(0, 100)
print(a, b, c, d, e, f)

# n = a
# for k in range(6): # отбросить последнюю цифру числа n
#   n = n // 10
#   print(n)

# n = a
# i = 0
# while n > 0:  # количество цифр
#   n = n // 10
#   i += 1
# print(i)

# #Определение НОД
# while a != b:
#   if a > b:
#     a = a - b
#   else:
#     b = b - a
# НОД = a
# print('НОД равен', НОД)

# n = 10
# while n < 100:
#   if n % 2 == 1:
#     print(n,'', end='')
#   n += 1

# n = a  # сумма цифр натурального числа
# sum = 0
# while n > 0:
#   dig = n % 10 # last number
#   sum += dig
#   n = n // 10
# print(sum)

# n = 10
# while n < 100:
#   if n * n < a:
#     print(n,'', end='')
#   n += 1

# n = 1
# while n < 100:
#   n += 1
#   if n * n < a:
#     print(n*n)

# while True:
#   print('Задайте значение коэффициента а уравнения:')
#   a = float(input())
#   if a != 0:
#     break  # досрочный выход из цикла

# for <всех значений в наборе>:
#   if <условие поиска значения> истинно:
#     break
# ...

# while True:
#   print('Задайте значение коэффициента а уравнения:')
#   a = float(input())
#   if 2 < a < 5:
#     print('very good - welcome')
#     break  # досрочный выход из цикла
#   elif a <= 2:
#     print('too small number')
#   elif a > 5:
#     print('too big number')

# while True:
#   print('enter password:')
#   a = float(input())
#   if a == 34567:
#     print('very good - welcome!!!')
#     break  # досрочный выход из цикла
#   else:
#     print('get out, please!!!')

# while True:
#   print('enter number:')
#   a = float(input())
#   if a == 0:
#     print('game over')
#     break  # досрочный выход из цикла
#   else:
#     print('enter more numbers!!!')

# x = a
# while True:
#   print('enter number:')
#   y = int(input())
#   if y * y > x:
#     print('ok - correct')
#     break  # досрочный выход из цикла
#   else:
#     print('enter other number!!!')
  