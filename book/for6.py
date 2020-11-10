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

# range(n) # n-последовательных целых чисел, начиная с 0
# range(1, n + 1) # конечное значение не используется
# range(a, b + 1) # при b > a
# range(a, b - 1, -1) # если b < a

# for n in range(10, 21):
#   print(n,'', end='')
# #10 11 12 13 14 15 16 17 18 19 20

# for n in range(50, 61):
#   print(n * n,'', end='')
# #2500 2601 2704 2809 2916 3025 3136 3249 3364 3481 3600

# for n in range(101):
#   if n % 10 == 5:
#     print(n,'', end='')
# #5 15 25 35 45 55 65 75 85 95

# s = 0 #Начальное значение переменной-сумматора
# for n in range(1, 101):
#   s = s + n
# print(s) #5050

# for n in range(10, 21):
#   print(n,'', end='')

# m = [1, 2, 3, 4, 5]
# for n in m:
#   print(n,'', end='')

# for n in range(10, a):
#   print(n ** 3)

# x = 0.453
# print('pounds', 'kg')
# for n in range(1, 11):
#   m = n * x
#   print(n,'  ', round(m, 3))
#pounds kg
#1    0.453

# x = 7
# for n in range(1, 10):
#   m = n * x
#   print(n,' x ', x,' = ',m)
# #1  x  7  =  7

# for n in range(10, 100):
#   if n % 2 == 1:
#     print(n)

# for n in range(10, 100):
#   if n % 10 == 3 or n % 10 == 7:
#     print(n,'', end='')

# for n in range(1000):
#   if n % a == 0:
#     print(n, a)

# for n in range(10, 100):
#   x = (n // 10) ** 2 + (n % 10) ** 2
#   if x % 13 == 0:
#     print(n, x)

# x = 0
# for n in range(a):
#   x += n * n
# print(x)

# x = 0
# for n in range(2, 9):
#   x += (n - 1) * n
#   print(x)

# x = 0
# for n in range(100, 1000):
#   if n % 2 == 0:
#     x += n
# print(x)

# x = 0
# for n in range(100, 1000):
#   if ((n // 100 % 10) + (n // 10 % 10) + n % 10) == a:
#     x += 1
# print(x)

# x = 0
# y = 5
# for n in range(100, 1000):
#   if (((n // 100 % 10) + (n // 10 % 10) + n % 10) == y and 
#   n % y == 0):
#     x += 1
# print(x)

# # factorial nr.1
# k = 1
# for n in range(2, a+1):
#   k *= n
#   print(k)

# # factorial nr.2
# n = randint(1, 20)
# k = 1
# while n > 1: # cicle
#   k *= n
#   n -= 1
# print(k)

# # factorial nr.3
# def fac(n): # recurcia
#   if n == 0:
#     return 1
#   return fac(n - 1) * n
# print(fac(5))

# # factorial nr.4
# print(math.factorial(20))

# for n in range(10):
#   print(20,'', end='')

# x = 13
# y = 3.67
# m = 0
# for n in range(x):
#   m += y
#   print(round(m, 3))

# x = 1
# y = 3
# print('hour', 'units')
# for n in range(1, 10):
#   x += x
#   m = n * 3
#   print(m, x)

# # Fibonacci
# x = 1
# y = 1
# z = y + x
# x = y
# y = z
# z = y + x
# print(z)

# x = y = 1
# print(x, y)
# i = 2
# for n in range(10): # for
#   x, y = y, x + y
#   print(y, end='')
#   i += 1
#   print()

# n = int(input())
# f1 = f2 = 1
# print(f1, f2, end=' ')
# i = 2
# while i < n:
#   f1, f2 = f2, f1 + f2
#   print(f2, end=' ')
#   i += 1
# print()

# for z in range(20000000): # обеспечения некоторой паузы
#   а = 30000 # aprox. 5 sec.