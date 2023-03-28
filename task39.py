# Задача №39. 
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
def cross_arrays(input_arr_1, input_arr_2):
  second_set = set(input_arr_2)
  result = []
  for i in input_arr_1:
    if i not in second_set:
      result.append(i)
  return result

len_first_arr = int(input('Введите длинну первого массива: '))
first_arr =[]
for i in range(len_first_arr):
  first_arr.append(input(f'Введите {i + 1}-й элеент первого массива: '))
  
len_second_arr = int(input('Введите длинну второго массива: '))
second_arr =[]
for i in range(len_second_arr):
  second_arr.append(input(f'Введите {i + 1}-й элеент второго массива: '))
  
print(cross_arrays(first_arr, second_arr))