# 11. Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое
# число n, что φ(n)=A. Если А не является числом Фибоначчи, 
# выведите число -1.

num = int(input('Введите натуральное число: '))
f1 = 0
f2 = 1
temp_fib = f1 + f2
count = 3
while temp_fib != num:  
  f1 = f2
  f2 = temp_fib
  temp_fib = f1 + f2
  count += 1
if temp_fib == num:
  print(count)
else:
  print(-1)

