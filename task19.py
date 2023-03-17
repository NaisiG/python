# Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

input_list = []
list_len = int(input('Введите кол-во элементов в списке: '))
for _ in range(list_len):
  input_list.append(int(input(f'Введите число: ')))
print(input_list)

input_k = -int(input('Введите число сдвига: '))

while input_k > len(input_list):
  input_k = input_k - len(input_list)

input_list = input_list[-input_k:] + input_list[:-input_k]
print(input_list)