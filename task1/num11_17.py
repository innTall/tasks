# 1.11. Составить программу, которая запрашивает название футбольной команды
# и повторяет его на экране со словами « – это чемпион!».

print('what fc win championat?')
name = input()
print(f'{name} - is champion!')

# 1.12. Напишите программу, в которую вводится имя человека и выводится на
# экран приветствие в виде слова «Привет», после которого должна стоять
# запятая, введенное имя и восклицательный знак. После запятой должен стоять
# пробел, а перед восклицательным знаком пробела быть не должно.

name = input()
print(f'Hello, {name}!')

# 1.13. Напишите программу, в которую вводится целое число, после чего на
# экран выводится следующее и предыдущее целое число. Например, при вводе
# числа 15 на экран должно быть выведено:
# Следующее за числом 15 число – 16.
# Для числа 15 предыдущее число – 14.

x = int(input())
y = x + 1
z = x - 1
print(f'next number of {x} is {y},\n for {x} last number is {z}')

# 1.14. Составить программу вывода на экран в одну строку трех любых чисел,
# вводимых с клавиатуры, с двумя пробелами между ними.
# 1.15. Составить программу вывода на экран в одну строку четырех любых
# чисел, вводимых с клавиатуры, с одним пробелом между ними.

x = int(input())
y = int(input())
z = int(input())
print(x, y, z, sep='--')

# 1.16. Составить программу вывода на экран следующей информации:
# а) 5 10       б) 100 t         в) x 25
#    7 см          1949 v           x y
# Примечание   t, v, x и y – переменные величины целого типа, значения
# которых вводятся с клавиатуры и должны быть выведены вместо имен величин.

a = int(input())
b = int(input())
c = int(input())
print(a, b,'\n', c, 'cm')

# 1.17. Составить программу вывода на экран следующей информации:
# а) 2 кг       б) а 1       в) x y
#    13 17         19 b         5 y
# Примечание    a, b, x и y – переменные величины целого типа, значения
# которых вводятся с клавиатуры и должны быть выведены вместо имен величин.

