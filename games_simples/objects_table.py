'''
Описание игры. На столе выложены n предметов (спичек, монет, камешков и т. п.).
Играют двое. Они поочередно забирают несколько предметов, причем заранее
договорено, что число забранных предметов не превышает k (1 < k ≤ n).
Проигрывает тот, кто своим ходом вынужден забрать последний предмет (или тот,
кто своим ходом заберет все оставшиеся предметы).
Разработаем программу, которая моделирует эту игру. Будут играть человек и
компьютер. Сразу же заметим, что в игре имеется выигрышная тактика (то есть
тактика, следуя которой, можно обеспечить себе победу при определенных условиях).
'''

from random import randint
import time
# 1. Вводная часть
n = randint(15, 30)  # начальное количество предметов n
print('Total', n, 'objects')
for i in range(n):
  print('@ ', end='')

k = randint(3, 5) # макс количество предметов за один раз
print()
print('one time can take max -', k, 'objects')

order = randint(1, 2) # определение очередности
if order == 1:
  print('Start comp')
else:
  print('Start YOU')

z = 0
# 2. Основная часть. Ее схема:
while True:
  if order == 1: #Ход компьютера
    if n >= k:
      units1 = randint(1, k) #выбор компьютера - мах k
    else: # n < k
      units1 = randint(1, n) #Берет не больше n
    time.sleep(2)
    print('comp take ',units1)
    n = n - units1
  else: #Ход человека
    time.sleep(2)
    while True:
      units2 = int(input('how many you take? - ')) # выбор человека
      if units2 < 1 or units2 > k:
        z += 1
        print('Atension! Enter from',1,'to',k,'! Press other button')
        if z == 3: print('Do you stupid? Press from',1,'to',k)
      else:
        break # exit of cicle
    n = n - units2
  
  if order == 1:  # Cледующий ход делает другой участник игры
    order = 2
  else:
    order = 1  
  
  if n == 0:  # Проверяем, не закончилась ли игра
    if order == 2:
      print('Last object take comp - winner YOU! Congratulation!!!')
    else:
      print('Last object take you - winner COMP!')
    break  # Прекращаем все действия
  else: #Игра продолжается
    time.sleep(2)
    print('Now left -:',n,'objects') # информация об оставшихся предметах


# Всю программу, моделирующую игру, «соберите» самостоятельно.
# Предусмотрите в ней:
# • паузы между отдельными этапами программы;
# • проверку правильности введенного участником игры значе-
# ния на этапе 1 (см. игру 7.1).