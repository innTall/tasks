from random import randint, uniform
import math
# print(f'd = {d}')
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
d = randint(0, 100)
print(a, b, c, d)

# 1.1. Вывести на одной строке 4 числа с одним пробелом между ними.

#print(a, b, c, d) # ok
print('{: 5d}{: 5d}{: 5d}{: 5d}'.format(a, b, c, d))

# 1.2. Вывести на одной строке 4 числа с двумя пробелами между ними.

#print(a, b, c, d, sep='  ') # пробелы или символы

# 1.3. Вывести на экран числа 50 и 10 одно под другим.
# 1.4. Вывести на экран числа 5, 10 и 21 одно под другим.

#print(a,'\n', b,'\n', c,'\n', d, sep='') # ok

# 1.5. Получить на экране следующее:

#print('\n', 1, '\n', '\n', 2, sep='') # ok

# 1.6. Число π примерно равно 3.1415926. Вывести это число в виде 3.142

# x = round(math.pi, 3) # ok
# print(x)

#x = math.pi 
#print('% .3f '% x)

# print('{:.3f}'.format(math.pi))
# print('{: .3f}'.format(math.pi))
# print('{: 10.3f}'.format(math.pi)) # ok (смотреть пробелы)

# 1.7. Число e приблизительно равно 2.71828. Вывести это число в виде 2.7

# x = round(math.e, 2) # ok
# print(x)

# x = math.e # ok
# print('% .2f '% x)

# print('{:.2f}'.format(math.e))
# print('{: .2f}'.format(math.e))
# print('{: 6.2f}'.format(math.e)) # ok (смотреть пробелы)

# 1.8. Составить программу вывода на экран числа, вводимого с клавиатуры.
# Выводимому числу должно предшествовать сообщение «Вы ввели число».

# print('enter number ')
# x = int(input())
# print('entered number is', x)
# print(f'entered number is {x}') # ok

# 1.10. Составить программу, которая запрашивает имя человека
# и повторяет его на экране.

# print('what is you name?')
# name = input()
# print('hello,', name, '$')
# print(f'Hello, {name}') # ok (смотреть пробелы и запятые)

# 1.9. Составить программу вывода на экран числа, вводимого с клавиатуры.
# После выводимого числа должно следовать сообщение «– вот какое число Вы ввели».

# 1.11. Составить программу, которая запрашивает название футбольной команды
# и повторяет его на экране со словами « – это чемпион!».

# print('what fc win championat?')
# name = input()
# print(name, '- is Champion!!!')
# print(f'{name} - is champion!') # ok

# 1.12. Напишите программу, в которую вводится имя человека и выводится на
# экран приветствие в виде слова «Привет», после которого должна стоять
# запятая, введенное имя и восклицательный знак. После запятой должен стоять
# пробел, а перед восклицательным знаком пробела быть не должно.

# name = input()
# print('hello, ', name,'!', sep='')
# print(f'Hello, {name}!') # ok (смотреть пробелы и запятые)

# 1.13. Напишите программу, в которую вводится целое число, после чего на
# экран выводится следующее и предыдущее целое число. Например, при вводе
# числа 15 на экран должно быть выведено:
# Следующее за числом 15 число – 16.
# Для числа 15 предыдущее число – 14.

# x = int(input())
# y = x + 1
# z = x - 1
# print('Next number of ', x, ' is ', y, ',', '\n', 'for ', x, ' last number is ', z, sep='')
# print(f'next number of {x} is {y},\n for {x} last number is {z}', sep='')

# 1.14. Составить программу вывода на экран в одну строку трех любых чисел,
# вводимых с клавиатуры, с двумя пробелами между ними.
# 1.15. Составить программу вывода на экран в одну строку четырех любых
# чисел, вводимых с клавиатуры, с одним пробелом между ними.

# x = int(input())
# y = int(input())
# z = int(input())
# print(x, y, z, sep='--')  # ok
#print('{: 5d}{: 5d}{: 5d}'.format(x, y, z))

# 1.16. Составить программу вывода на экран следующей информации:
# а) 5 10       б) 100 t         в) x 25
#    7 см          1949 v           x y
# Примечание   t, v, x и y – переменные величины целого типа, значения
# которых вводятся с клавиатуры и должны быть выведены вместо имен величин.

# a = int(input())
# b = int(input())
# c = int(input())
# print(a, b,'\n', c, ' cm', sep='',)

# 1.17. Составить программу вывода на экран следующей информации:
# а) 2 кг       б) а 1       в) x y
#    13 17         19 b         5 y
# Примечание    a, b, x и y – переменные величины целого типа, значения
# которых вводятся с клавиатуры и должны быть выведены вместо имен величин.
