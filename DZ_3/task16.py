# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число n – количество элементов в массиве.
# В последующих  строках записаны n целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count). 
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1


list_n = []
N = int(input("Введите размер массива: "))     
num2 = 0
if N > 1000 and N >= -1000:
    print("Число больше 1000!")
    exit()
else:
    for i in range(N):
        num = int(input("Введите число в массив: "))
        if num >= 1000 or num < -1000:
            pass
        else:
            list_n.append(num)
    num2 = int(input("Введите число для поиска в массиве: "))
 
print(f'Число {num2} встречается в списке {list_n.count(num2)} раз')


vowels = [1, 2, 3, 3, 4, 5]      # count метод
count = vowels.count(3) 
print('Число 3 встречается:', count)


import time

start = time.perf_counter()
print(f'Число {num2} встречается в списке {list_n.count(num2)} раз')
print('Число 3 встречается:', count)
end = time.perf_counter()
first_time = end - start
print(first_time)