from random import randint, uniform
import math
# print(f'd = {d}')
a = uniform(-10, 10)
b = uniform(-10, 10)
c = uniform(-10, 10)
d = uniform(-10, 10)
print(a, b, c, d)

# 4.1. Даны два различных вещественных числа. Определить:
# а) какое из них больше;
# б) какое из них меньше.

# x = a - b
# if x > 0: 
#   print(f'a > b')
# else:
#   print(f'a < b')

# 4.2. Рассчитать значение у при заданном значении х:

x = a
if x > 0: y = math.sin(x) * math.sin(x)
else: y = (1 - 2 * math.sin(x * x))
#print(x, y)

# 4.3. Рассчитать значение у при заданном значении х:

x = a
if x > 0: y = math.sin(x * x)
else: y = (1 + 2 * math.sin(x) * math.sin(x))
#print(x, y)

# 4.4. Определить, в какую из областей – I или II (рис. 4.1) – попадает точка
# с заданными координатами. точка не попадает на границу областей.

# x = a
# if x > 4: print('x in II')
# else: print('x in I')

# 4.5. Определить, в какую из областей – I или II (рис. 4.2) – попадает точка
# с заданными координатами, точка не попадает на границу областей.

# y = a
# if y > 3: print('y in I')
# else: print('y in II')

# 4.6. Для функций, заданных графически (рис. 4.3), определить
# значение у при заданном значении х.

x = a
if x <= 2: y = x
else: y = 2
#print(y)

x = a
if x <= 3: y = x * -1
else: y = -3
#print(y)

# 4.7. Составить программу для вычисления значения функции f(x):
# 4.8. Составить программу для вычисления значения функции f(x):

x = a
if math.sin(x) < 0:
  k = x * x
else:
  k = abs(x)
#print(k)

if k < x: f = k * x
else: f = k + x
#print(f)

# 4.9. Определить макс и мин значения из двух различных вещественных чисел.
# Использовать один условный оператор.

# x = a - b
# if x > 0: 
#   print(f'a >> max')
# else:
#   print(f'a >> min')

# 4.10. Известны два расстояния: одно выражено в километрах,
# другое – в футах (1 фут = 0,3048 м). Какое из расстояний меньше?
# 4.11. Известны две скорости: одна выражена в километрах
# в час, другая – в метрах в секунду. Какая из скоростей больше?

# x = abs(a)
# y = abs(b * 0.3048)
# if x - y > 0:
#   print('x > y')
# else:
#   print('x < y')

# 4.12. Даны радиус круга и сторона квадрата. У какой фигуры площадь больше?

r = abs(a)
t = abs(a)
s1 = math.pi * r * r
s2 = t * t
#print(s1, s2)

# 4.13. Даны объемы и массы двух тел из разных материалов.
# Материал какого из тел имеет большую плотность?
# 4.14. Известны сопротивления двух не соединенных друг
# с другом участков электрической цепи и напряжение на каждом
# из них. По какому участку протекает меньший ток?
# 4.15. Даны коэффициенты a, b и c квадратного уравнения
# aх2 + bx + c = 0 (а ≠ 0). Выяснить, имеет это уравнение корни или
# нет (сами корни, если они есть, вычислять не нужно).
# 4.16. Для условий предыдущей задачи в случае наличия ве-
# щественных корней найти их, в противном случае – вывести на
# экран соответствующее сообщение. Вариант равенства корней от-
# дельно не рассматривать.
# 4.17. Известны год и номер месяца рождения человека, а также год и номер
# месяца сегодняшнего дня (январь – 1 и т. д.). Определить возраст человека
# (число полных лет). В случае совпадения указанных номеров месяцев считать,
# что прошел полный год.

x1 = 1967
x2 = 2020
y1 = 4
y2 = 10
z1 = (x2 - x1) * 12 - 4 + 10
z2 = z1 // 12
#print(z1, z2)

# 4.18. Известны площади круга и квадрата. Определить:
# а) уместится ли круг в квадрате?
# б) уместится ли квадрат в круге?

s = 50
r = math.sqrt(s / math.pi)
d = r * 2
l = math.sqrt(s)
print(r, d, l)

# 4.19. Известны площади круга и равностороннего треугольни-
# ка. Определить:
# а) уместится ли круг в треугольнике?
# б) уместится ли треугольник в круге?

# 4.20*. Даны два прямоугольника, стороны которых параллель-
# ны или перпендикулярны осям координат. Известны координаты
# левого нижнего и правого нижнего углов каждого из них. Найти
# координаты левого нижнего и правого верхнего углов минималь-
# ного прямоугольника, содержащего указанные прямоугольники.

# 4.21*. Даны два прямоугольника, стороны которых параллель-
# ны или перпендикулярны осям координат. Известны координаты
# левого нижнего угла каждого из них и длины их сторон. Найти
# координаты левого нижнего и правого верхнего углов минималь-
# ного прямоугольника, содержащего указанные прямоугольники.
