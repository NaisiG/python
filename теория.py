# map, filter, zip, lambda, enumerate


# some_list = [1, 2, 3, 4, 5]
# print(list(map(lambda a: a ** 2, some_list)))    # map - функция

# print(list(filter(lambda x: x % 2 == 0, some_list)))  #filter - условие

# some_list = [1, 2, 3, 4, 5]
# some_list2 = ['1', '2', '3', '4', '5']
# print(list(zip(some_list, some_list2)))   # zip- объединяет все объекты по индексу в картежи (по мин кол-ву индексов)

# for i, j in zip(some_list, some_list2):
#   print(i, j)

# some_list = [1, 2, 3, 4, 5]
# print(list(enumerate(some_list)))    # enumerate - используются индексы и значения

#Посмотреть иттераторы и генираторы