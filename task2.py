# 2. Одинаковая четность
# Даны два целых числа: А и В. 
# Проверитиь истинноссть высказывания: "Числа А и В имеют одинаковую четность".

a = int(input('Введите целое число A: '))
b = int(input('Введите целое число B: '))

if a % 2 == 0 and b % 2 == 0:
  print("Одинковая четность")
elif a % 2 != 0 and b % 2 != 0:
  print("Одинковая четность")
else:
  print("Не верно!")