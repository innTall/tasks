from random import randint
import time

'''
Игра моделирует бросание игрального кубика каждым из двух участников, после
чего определяется, у кого выпало больше очков.
В программе используем переменные:
player1 -
player2 -
n1 - digit of cube player1
n2 – digit of cube player2
s - points for win
i1 - total of points player1
i2 - total of points player2
• функция sleep() from module time, for made pause in work the programm
'''
s = 10
i1 = 0
i2 = 0
#Ввод имен играющих
player1 = input('What is your name? ')
player2 = input('What is your name? ')
#Моделирование бросания кубика первым играющим
for k in range(s):
  print('Throw cube ', player1)
  time.sleep(1)
  n1 = randint(1, 6)
  i1 += n1
  print('     Points: ', n1)
  #Моделирование бросания кубика вторым играющим
  print('Throw cube', player2)
  time.sleep(1)
  n2 = randint(1, 6)
  i2 += n2
  print('     Points:', n2)
  time.sleep(1)
  print(player1,':',player2)
  print('% 3d '% i1, '% 4d '% i2)
#Определение результата (3 возможных варианта)
if i1 > i2:
  print('Winner', player1)
elif i1 < i2:
  print('Winner', player2)
else:
  print('Ничья')
