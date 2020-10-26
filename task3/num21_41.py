from random import randint, uniform
import math
# print(f'd = {d}')
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
d = randint(0, 100)
print(a, b, c, d)

# 3.21. (111). Переставить его цифры справа налево.
# 3.22. (111). В нем зачеркнули первую слева цифру и приписали ее в конце.
# 3.23. (111). В нем зачеркнули последнюю справа цифру и приписали ее в начале.
# 3.24. (111). Переставить первую и вторую цифры заданного числа.
# 3.25. (111). Переставить вторую и третью цифры заданного числа.
# 3.26. (111). Все цифры различны, переставить - из него шесть разных чисел.

x = 345
e = x % 10
d = x // 10 % 10
s = x // 100

v21 = e * 100 + d * 10 + s
v22 = d * 100 + e * 10 + s
v23 = e * 100 + s * 10 + d
v24 = d * 100 + s * 10 + e
v25 = s * 100 + e * 10 + d
#print(x, v21, v22, v23, v24, v25)

# 3.27. Написать программу, в которой рассчитывается:
# а) сумма цифр (1111), (11111) вводимого с клавиатуры.
# 3.28. Дано (1111). Разные варианты перестановок.
# г) переставить пары цифр (2 способа: 1234 = 3-4-1-2, 1234 = 34-12

x = a * 43
if 1000 < x < 10000:
  e = x % 10
  d = x // 10 % 10
  s = x // 100 % 10
  t = x // 1000
  v = e + d + s + t
  f = d * 1000 + e * 100 + t * 10 + s
  gg1 = x // 100
  gg2 = x % 100
  g = gg2 * 100 + gg1
  #print(x, e, d, s, t, v, f, gg1, gg2, g)

x = a * 521
if 10000 < x < 100000:
  e = x % 10
  d = x // 10 % 10
  s = x // 100 % 10
  k = x // 1000 % 10
  t = x // 10000
  v = e + d + s + k + t
  #print(x, e, d, s, k, t, v)

# 3.29. Дано натуральное число n (n > 9). Найти:
# а) число единиц в нем;
# б) число десятков в нем.
# 3.30. Дано натуральное число n (n > 99). Найти:
# а) число десятков в нем;
# б) число сотен в нем.
# 3.31. Дано натуральное число n (n > 999). Найти:
# а) число сотен в нем;
# б) число тысяч в нем.

n = a * 543
e = n % 10
d = n // 10 % 10
s = n // 100 % 10
k = n // 1000 % 10
t = n // 10000
#print(n, t, k, s, d, e, sep='-')

# 3.32. Из (111) x вычли его последнюю цифру. Когда результат разделили на 10,
# а к частному слева приписали последнюю цифру числа x, то получилось число 237.
# 3.33. Из (111) x вычли его последнюю цифру. Когда результат разделили на 10,
# а к частному слева приписали последнюю цифру числа x, то получилось число n.

x = a * 13
if 100 < x < 1000:
  # e = x % 10
  # d = x - e
  # g10 = d / 10
  # y = int(e * 100 + g10)
  y = int((x % 10) * 100 + (x - e) / 10)
  #print(x, y, sep=' >> ')

# 3.34. В (111) x зачеркнули первую цифру. Когда оставшееся число умножили на
# 10, а произведение сложили с первой цифрой числа x, то получилось число 564.
# 3.35. В (111) x зачеркнули первую цифру. Когда полученное число умножили на
# 10, а произведение сложили с первой цифрой числа x, то получилось число n.

x = a * 13
if 100 < x < 1000:
  # s = x // 100
  # de = (x % 100) * 10
  # g = x % 100
  # g10 = g * 10
  # x = g10 + f
  n = (x % 100) * 10 + x // 100
  #print(x, n, sep=' >> ')

# 3.36. В (111) x зачеркнули его вторую цифру. Когда к образованному при этом
# двузначному числу слева приписали вторую цифру числа x, то получилось число 546.
# 3.37. В (111) x зачеркнули его вторую цифру. Когда к образованному при этом
# двузначному числу слева приписали вторую цифру числа x, то получилось число n.

x = a * 13
if 100 < x < 1000:
  # e = x % 10
  # d = x // 10 % 10
  # s = x // 100
  # se = s * 10 + e
  # v = d * 100 + se
  n = (x // 10 % 10) * 100 + (x // 100) * 10 + x % 10
  #print(x, n, sep=' >> ')

# 3.38. В (111) x зачеркнули его вторую цифру. Когда к образованному при этом
# двузначному числу справа приписали вторую цифру числа x, то получилось число 456.
# 3.39. В (111) x зачеркнули его вторую цифру. Когда к образованному при этом
# двузначному числу справа приписали вторую цифру числа x, то получилось число n. 

x = a * 13
if 100 < x < 1000:
  # e = x % 10
  # d = x // 10 % 10
  # s = x // 100
  # se = s * 10 + e
  # v = se * 10 + d
  n = ((x // 100) * 10 + (x % 10)) * 10 + x // 10 % 10
  #print(x, n, sep=' >> ')

# 3.40. В (111) x зачеркнули его последнюю цифру. Когда в оставшемся двузначном
# числе переставили цифры, а затем приписали к ним слева последнюю цифру числа
# x, то полу# чилось число 654. Найти число x.
# 3.41. В (111) x зачеркнули его последнюю цифру. Когда в оставшемся двузначном
# числе переставили цифры, а затем приписали к ним слева последнюю цифру числа
# x, то получилось число n.

x = a * 13
if 100 < x < 1000:
  e = x % 10
  d = x // 10 % 10
  s = x // 100
  ds = d * 10 + s
  v = ds * 10 + e
  n = ((x // 10 % 10) * 10 + x // 100) * 10 + x % 10 
  #print(x, n, sep=' >> ')
