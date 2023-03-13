# num = int(input())
# sum = 0
# while num > 0:
#   sum += num % 10
#   num //= 10
# print(sum)

# for letter in 'привет':
#   print(letter)

# for i in range(5,10, 2):
#   print(i)

#Переменная итератор используется
# for i in range(1,11, 2):
#   print(i ** 2)

#Переменная итератор не используется   '_'-переменная
# for _ in range(5):
#   print('hello')

# a = 'hello'
# for i in range(0, len(a), 2):   #0, 2, 4
#   print(a[i])   #end = '\n' - вывод в одну линию

# 9. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

num = int(input('Введите число N: '))
fact = 1
while num > 0:
  fact *= num
  num -= 1
print(fact)
  



