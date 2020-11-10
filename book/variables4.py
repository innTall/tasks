from random import randint, uniform
import math
# print(f'd = {d}')
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
d = randint(0, 100)
print(a, b, c, d)

# а = input() # инструкции ввода данных

# surname = input('write last name: ')
# name = input('write name: ')

# print('write surname and name: ')
# surname = input()
# name = input()

# print('write string of symbols', end = '')
# st = input() # ввод и вывод в одной строке

# z = a//b
# m = a % b
# print(z, m)

# x, y, z = 7, 2, -5
# a = b = 0

# #Ввод исходных данных
# print('Задайте первое число')
# a = int(input())
# print('Задайте второе число')
# b = int(input())

# print('Задайте вещественное число')
# z = float(input())

# а = int(input('Введите целое число '))
# z = float(input('Задайте вещественное число '))

# club = 'Real'
# my_club = club

# im = 'Dima'
# im2 = im.upper() #О методе upper() см. главу 3

# fullname = name + surname

# x, y = y, x

# print('write the name: ')
# name = input()
# print('hello, ', name,'!', sep='')
# hello, tom!

# print('write any number: ')
# x = int(input())
# y = x + 1
# z = x - 1
# print('next number: ', y,'.','\n', 'before number: ', z,'.', sep='')
# next number: 24.
# before number: 22.

# print('write two numbers:')
# x = int(input())
# y = int(input())
# print('x+y=',x+y, ' x-y=',x-y, ' x*y=',x*y, ' x/y=',x/y, ' (x+y)/2=',(x+y)/2,
# sep='')

# print('write any nymber:')
# x = int(input())
# print('summ =', x // 10 + x % 10)

# print('write any nymber:')
# x = int(input())
# print(x // 100,', ', x // 10 % 10,', ', + x % 10, sep='')
# 5, 6, 7

# print('write any number:')
# x = int(input())
# y = int(input())
# print(x, 'summ =', x//1000+x//100%10+x//10%10+x%10)
# print(y, 'summ =', y//10000+y//1000%10+y//100%10+y//10%10+y%10)
# #5678 summ = 26
# #12345 summ = 15

# import math # from math import sqrt, sin, cos
# n = math.sqrt((a + b)/2)
# print(round((n), 3))

#print(int(math.sqrt(a * a + b * b)))

dx = a - b
dy = c - d
d = math.sqrt(dx * dx + dy * dy)
print(round(d, 2))
