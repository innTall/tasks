from random import randint, uniform
import math
# print(f'd = {d}')
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
d = randint(0, 100)
print(a, b, c, d)

print(1, '. Площадь прямоугольника равна', a, 'кв. см')
#1 . Площадь прямоугольника равна 56 кв. см

print('%.3f '% math.pi) # пробел перед точкой - отступ строки
#3.142

print('% 7.3f '% math.pi) # 7 общее количество позиций экрана
#  3.142

print('% 6.2f '% math.pi, '% 6.2f '% math.e)
#  3.14    2.72

s = a + b
print('Сумма равна', '% 8d '% s)
#Сумма равна       92

a = 5; b = 3
print('f(', b, ') = ',a, sep = '')
#f(3) = 5

a = 5; b = 3
print('f(a)=', '(b)', sep = '')
#f(a)=(b)

a = 5; b = 3
print('f(', a, ')=(', b, ')', sep = '')
#f(5)=(3)

print('three numbers: ', d, d, d, sep=' ')
#three numbers:  45 45 45

print('three numbers: ', d,', ', d,', ', d, sep='')
#three numbers: 66, 66, 66

print('{: 10.2f}'.format(math.pi))
#      3.14

print ('{: 5d}'.format(d))
#   31

a = 1/3
b = 1/9
print('{: 7.3f}{: 7.3f}'.format(a, b))
#  0.333  0.111

print('{: 5.1f}{: 5.1f}'.format(1/3, 1/7))
#  0.3  0.1

x = 317
y = 123
z = 72
print('{: 5d}{: 5d}{: 5d}'.format(x, y, z))
#  317  123   72