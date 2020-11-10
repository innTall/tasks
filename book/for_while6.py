from random import random, randint, uniform
#import pandas as pd
#import numpy as np
import math
# print(f'd = {d}')
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
d = randint(0, 100)
e = randint(0, 100)
f = randint(0, 100)
print(a, b, c, d, e, f)

# for x in range(10, 21):
#   print(x)

# x = 10
# while x != 21: # аналогичная инструкция for
#   print(x)
#   x = x + 1

# n = 1
# while n <= 31:
#   print(n * n)
#   n = n + 2

# for n in range(1, 32, 2):  # аналогичная инструкция while
#   print(n * n)

# k = 0  # количество цифр некоторого натурального числа
# while n > 0:  # аналогичной инструкции for нет
#   n = n//10
#   k = k + 1

# for x in range(100, 79, -1):
#   print(x)

# x = 100
# while x != 79:
#   print(x)
#   x -= 1

# n = 21
# while n <= 151:
#   print(2 * n)
#   n = n + 10

# for x in range(21, 152, 10):
#   print(2 * x)

# n = 2
# while n <= 12:
#   print(n)
#   n = n + 0.5

# for x in range(2, 13, 0.5): # ??? float - int
#   print(x)

# x = a  # Найти все натуральные делители для x, меньше y
# y = b
# #Способ 1 - не хороший вариант
# #x = int(input('x = '))
# #y = int(input('y = '))
# for vdel in range(1, x + 1):
#   if x % vdel == 0: #Встретился делитель числа n
#     if vdel <= y:  # Сравниваем его с m
#       print(vdel)

# for vdel in range(2, x + 1):  # укороченная версия способа 1
#   if x % vdel == 0 and vdel <= y:
#     print(vdel)

# #Способ 2 - способ лучше - недостаток убран с помощью break
# for vdel in range(1, x + 1):
#   if x % vdel == 0 and vdel <= y:
#     print(vdel)
#   if vdel > y:
#     break

# #Способ 3
# vdel = 1
# while vdel <= y:
#   if x % vdel == 0:
#     print(vdel)
#   vdel += 1

# наименьший натуральный делитель, отличный от 1
# n = a
# #Способ 1 - недостаток - проверки проводятся даже после нахождения
# #n = int(input('n = '))
# var1 = False #Или var1 = 0
# # все числа, большие 1, которые могут быть делителем числа n
# for vdel in range(2, n + 1):
#   #Проверяем, является ли число vdel делителем числа n
#   if n % vdel == 0: #Если является, то - это первый делитель? 
#     #Если не было
#     if var1 == False: #Или if var1 == 0:
#       #Встретился искомый делитель - Выводим его на экран
#       print(vdel)
#       #Искомый делитель найден – меняем значение переменой var1
#       var1 = True #Или var1 = 1

# #Способ 2 - условия продолжения цикла - var1 == False
# #n = int(input('n = '))
# vdel = 2 #Начальные
# var1 = False #значения
# while var1 == False:
#   if n % vdel == 0:
#     print(vdel)
#     var1 = True
#   #Переходим к следующему числу
#   vdel = vdel + 1

# n = a
# #Способ 3 - аналог инструкции цикла с постусловием
# #n = int(input('n = '))
# vdel = 2
# while True:
#   if n % vdel == 0:
#     print(vdel)
#     break
#   vdel = vdel + 1

# n = a
# #Способ 4
# #n = int(input('n = '))
# for vdel in range(2, n + 1):
#   if n % vdel == 0: #Встретился искомый делитель
#     print(vdel)
#     break #Выход из цикла

# m = a
# # числа Фибо, не превышающие числа m
# #m = int(input('m = '))
# #Выводим первые 2 числа последовательности
# print('1 1 ', end ='')
# #Определяем и выводим остальные числа
# pred = 1
# predpred = 1
# while pred + predpred <= m: #Обратите внимание на условие
#   ocher = pred + predpred
#   print(ocher, end = ' ')
#   predpred = pred
#   pred = ocher

# # интервал чисел для расчетов явно не задан - его рассчитать
# n = a
# #n = int(input('n = '))
# for k in range(1, int(math.sqrt(n)) + 1):
#   print(k)

# # упрощенный вариант решения - замена for на while
# n = a
# #n = int(input('n = '))
# k = 1
# while k * k <= n:
#   print(k)
#   k = k + 1

# n = a
# #n = int(input('n = '))
# for k in range(1, int(math.sqrt(n)) + 1):
#   print(k * k)
# # или
# k = 1
# while k * k <= n:
#   print(k * k)
#   k = k + 1

x = random()
0 < x <= 1 Из чисел 1, 1/2, 1/3, ... напечатать те, которые > x

for n in range(1, 0, -1/n):

x = uniform(0, 2)
1 < x <= 1.5 Из чисел 1+1/2, 1+1/3, ... напечатать те, которые > x
Числа представляют собой сумму 1+1/n (n = 2, 3,...) и образуют
убывающую последовательность.

Вывести первое натуральное число - x * x > n. x < 100.

Дано число x (0 < x ≤ 1). Из чисел 1, 1/2, 1/3,... найти первое
число, которое меньше x.

