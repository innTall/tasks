from random import randint

'''
Описание игры. Компьютер генерирует случайное целое число 0 < x < 101. Играющий
пытается отгадать это число, делая несколько попыток. В случае несовпадения
«задуманного» компьютером числа и числа-ответа на экран выводится сообщение о
том, какое из них больше, после чего играющий вновь вводит число, и т. д.
до отгадывания.
В приведенной ниже программе использованы следующие величины:
• n_comp – число, генерируемое компьютером;
• otvet – число, называемое играющим;
• n – количество названных чисел до отгадывания (включая отгаданное число);
эта величина представляет собой «счетчик».
'''
n_comp = randint(1, 100)
print('Компьютер "загадал" число в интервале от 1 до 100. Какое?')
n = 0 #Счетчик числа попыток
while True: #Повторение попыток
  n = n + 1 #Номер очередной попытки
  otvet = int(input('Наберите это число '))
  if otvet > n_comp:
    print('Загаданное число меньше.')
  elif otvet < n_comp:
    print('Загаданное число больше.')
  else:
    print('Правильно! Число попыток до отгадывания -', n)
    break #Выход из цикла