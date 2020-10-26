from random import randint, uniform
import math
# print(f'd = {d}')
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
d = randint(0, 100)
print(a, b, c, d)

# Задачи повышенной сложности
# 3.42. Даны цифры двух целых чисел: двузначного a2a1 и однозначного b, где
# a1 – число единиц, a2 – число десятков. Получить цифры числа, равного сумме
# заданных чисел (известно, что это число двузначное). Слагаемое – двузначное
# число и число-результат не определять; условный оператор не использовать.

a1 = randint(1, 9)
a2 = randint(1, 9)
b = randint(1, 9)
t = a1 + a2 * 10 + b
e = t % 10
d = t // 10
#print(a1, a2, b, t, d, e)

# 3.43. Даны цифры двух двузначных чисел, записываемых в виде a2a1 и b2b1,
# где a1 и b1 – число единиц, a2 и b2 – число десятков.
# Получить цифры числа, равного сумме заданных чисел (известно, что это число
# двузначное). Слагаемое – двузначное число и число-результат не определять;
# условный оператор не использовать.

a1 = randint(1, 9)
a2 = randint(1, 9)
b1 = randint(1, 9)
b2 = randint(1, 9)
t = a1 + a2 * 10 + b1 + b2 * 10
e = t % 10
d = t // 10 % 10
s = t // 100
#print(a2, a1, b2, b1, t, s, d, e)

# 3.44. Даны цифры двух десятичных целых чисел: трехзначного a3a2a1 и
# двузначного b2b1, где a1 и b1 – число единиц, a2 и b2 – число десятков,
# a3 – число сотен. Получить цифры числа, равного сумме заданных чисел
# (известно, что это число трехзначное). Числа-слагаемые и число-результат
# не определять; условный оператор не использовать.

a1 = randint(1, 9)
a2 = randint(1, 9)
a3 = randint(1, 9)
b1 = randint(1, 9)
b2 = randint(1, 9)
t = a1 + a2 * 10 + a3 * 100 + b1 + b2 * 10
e = t % 10
d = t // 10 % 10
s = t // 100
#print(a3, a2, a1, b2, b1, t, s, d, e)

# 3.45. Даны целое число k (1 ≤ k ≤ 180) и последовательность цифр 10111213...9899,
# в которой выписаны подряд все двузначные числа. Определить:
# а) номер пары цифр, в которую входит k-я цифра;
# б) двузначное число, образованное парой цифр, в которую входит k-я цифра;
# в) k-ю цифру, если известно, что:
# – k – четное число;
# – k – нечетное число.
# Примечание  !!! Величины строкового типа не использовать.

k = randint(1, 180)
for x in range(10, 100):
  print(x, end='')
  #y = x[:k]
  #print(l)

# 3.46. Даны целое число k (1 ≤ k ≤ 150) и последовательность
# цифр 101102103...149150, в которой выписаны подряд все трех-
# значные числа от 101 до 150.
# Определить k-ю цифру, если известно, что:
# – k – число, кратное трем;
# – k – одно из чисел 1, 4, 7, ...;
# – k – одно из чисел 2, 5, 8, ...
# Примечание  !!! Величины строкового типа не использовать.

# 3.47. Даны целые числа h, m, s (0 < h ≤ 23, 0 ≤ m ≤ 59, 0 ≤ s # ≤ 59),
# указывающие момент времени: «h часов, m минут, s секунд». Определить угол
# (в градусах) между положением часовой стрелки в начале суток и в указанный момент времени.

# 3.48. С начала суток часовая стрелка повернулась на y градусов (0 ≤ y < 360,
# y – вещественное число). Определить число полных часов и число полных минут,
# прошедших с начала суток.

# 3.49. Часовая стрелка образует угол y с лучом, проходящим через центр и
# через точку, соответствующую 12 часам на цифербла# те, 0 < y ≤ 2p.
# Определить значение угла для минутной стрелки, а также количество полных часов и полных минут.

# 3.50. Даны целые числа h, m (0 < h ≤ 12, 0 ≤ m ≤ 59), указывающие момент
# времени: «h часов, m минут». Определить наи# меньшее время (число полных
# минут), которое должно пройти до того момента, когда часовая и минутная
# стрелки на циферблате:
# а) совпадут;
# б) расположатся перпендикулярно друг другу.

# 3.51. Даны два целых числа a и b. Если a делится на b или b делится на a,
# то вывести 1, иначе – любое другое число. Условные операторы и операторы цикла не использовать.