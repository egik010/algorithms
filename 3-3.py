# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

my_max = 0
my_min = array[0]
max_index = 0
min_index = 0

for i, line in enumerate(array):
    if my_max < line:
        my_max = line
        max_index = i
    if my_min > line:
        my_min = line
        min_index = i

print(f' Максимальное значение - {array[max_index]}, его индекс - {max_index}')
print(f' Минимальное значение - {array[min_index]}, его индекс - {min_index}')

array[max_index], array[min_index] = array[min_index], array[max_index]

print(array)
