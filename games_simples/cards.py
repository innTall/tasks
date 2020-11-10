'''
Игра моделирует выбор каждым из двух играющих «наугад» по одной карте из полного
набора игральных карт, включающего четыре масти («пики», «трефы», «бубны» и
«червы») и по 9 достоинств карт в каждой масти («шестерка», «семерка»,
«восьмерка», «девятка», «десятка», «валет», «дама», «король», «туз»), и
определение того из участников игры, у которого выбранная карта «старше». При
этом условимся, что приведенный выше перечень мастей и карт одной масти дан в
порядке увеличения их «старшинства» (например, любая карта масти «бубны» старше
любой карты масти «пики», а «валет червей» старше «десятки червей»).
При моделировании названиям мастей и названиям достоинства карты присвоены
условные номера:
• масти «пики» – 1, масти «трефы» – 2, масти «бубны» – 3, масти «червы» – 4;
• достоинствам: «шестерка» – 6, «семерка» – 7, …, «десятка» – 10,
«валет» – 11, «дама» – 12, «король» – 13, «туз» – 14.
'''
# сделать козырную масть
from random import randint
import time

n = 10
pl1 = 0
pl2 = 0
player1 = input('Enter your name: ')
player2 = input('Enter your name: ')
for k in range(n):
  num_symbol_1 = randint(1, 4)
  num_digit_1 = randint(6, 14)
  #3. Определение соответствующего названия масти:
  if num_symbol_1 == 1:
    symbol = 'пик'
  elif num_symbol_1 == 2:
    symbol = 'треф'
  elif num_symbol_1 == 3:
    symbol = 'бубен'
  else:
    symbol = 'червей'
  #и названия достоинства карты:
  if num_digit_1 == 6:
    digit = 'Шестерка'
  elif num_digit_1 == 7:
    digit = 'Семерка'
  elif num_digit_1 == 8:
    digit = 'Восьмерка'
  elif num_digit_1 == 9:
    digit = 'Девятка'
  elif num_digit_1 == 10:
    digit = 'Десятка'
  elif num_digit_1 == 11:
    digit = 'Валет'
  elif num_digit_1 == 12:
    digit = 'Дама'
  elif num_digit_1 == 13:
    digit = 'Король'
  else:
    digit = 'Туз'
  print(player1, '- card:', digit, symbol)
  time.sleep(2)

  num_symbol_2 = randint(1, 4)
  num_digit_2 = randint(6, 14)
  #3. Определение соответствующего названия масти:
  if num_symbol_2 == 1:
    symbol = 'пик'
  elif num_symbol_2 == 2:
    symbol = 'треф'
  elif num_symbol_2 == 3:
    symbol = 'бубен'
  else:
    symbol = 'червей'
  #и названия достоинства карты:
  if num_digit_2 == 6:
    digit = 'Шестерка'
  elif num_digit_2 == 7:
    digit = 'Семерка'
  elif num_digit_2 == 8:
    digit = 'Восьмерка'
  elif num_digit_2 == 9:
    digit = 'Девятка'
  elif num_digit_2 == 10:
    digit = 'Десятка'
  elif num_digit_2 == 11:
    digit = 'Валет'
  elif num_digit_2 == 12:
    digit = 'Дама'
  elif num_digit_2 == 13:
    digit = 'Король'
  else:
    digit = 'Туз'
  print(player2, '- card:', digit, symbol)
  time.sleep(2)

  if num_symbol_1 > num_symbol_2:
    pl1 += 1
    print('@ -',player1,'- @')
  elif num_symbol_2 > num_symbol_1:
    pl2 += 1
    print('@ =',player2,'= @')
  else: #Масти карт игроков одинаковые
    #Сравниваем достоинства карт (их номера)
    if num_digit_1 > num_digit_2:
      pl1 += 1
      print('<',player1,'>')
    elif num_digit_2 > num_digit_1:
      pl2 += 1
      print('<<',player2,'>>')
    else: #Достоинства карт тоже одинаковые3
      print('Ничья!')
  print(player1,':',player2)
  print('% 3d '% pl1, '% 4d '% pl2)
#Определение результата (3 возможных варианта)
if pl1 > pl2:
  print('WINNER', player1)
elif pl1 < pl2:
  print('WINNER', player2)
else:
  print('Ничья')