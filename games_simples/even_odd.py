from random import randint
'''
Описание игры. На экране появляется вопрос: «Чет (ввод 2) или нечет (ввод 1)?»
Играющий должен ответить, какое число – четное или нечетное – выберет компьютер,
и ввести соответственно 2 или 1. После этого компьютер случайным образом
генерирует одно из них. Результат сравнения ответа играющего с числом компьютера
выводится на экран.
Используемые переменные:
n - количество вопросов - должно быть нечетное число
q - победное количество - 1
ok - количество правильных ответов
i - проигрышные наборы
z - счетчик ошибочных вводов чисел
player – число, которое введет играющий в ответ на вопрос;
comp – число, которое «выберет» компьютер (здесь: comp = randint(1, 2)).
'''
n = 7
q = int(n / 2)
ok = 0
i = 0
z = 0
for k in range(n):
  if ok == i == q: print('fuck situation = last chanse')
  if ok == q + 1 or i == q + 1: continue
  while True:
    player = int(input('Even (press 2) or odd (press 1)? '))
    if player != 1 and player != 2:
      z += 1
      print('Atension! Enter 1 or 2! Press other button')
      if z == 3: print('Do you stupid? Press 1 or 2')
    else:
      break # exit of cicle
  comp = randint(1, 2)
  print('Number of computer:', comp)
  print('you - comp')
  if player == comp: #Сравнение
    ok += 1
  else:
    i +=1
  print('% 2d '% ok, '% 4d '% i)
#Определяем результат игры
if ok > n // 2:
  print('WOW, you WIN!!!',ok,':',i,'Do you want next game?')
else:
  print('you LOST...',ok,':',i,' is luser - may be revenge?')
