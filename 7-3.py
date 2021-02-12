# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
import statistics

MIN_MASS = 55
MAX_MASS = 200
m = random.randint(MIN_MASS, MAX_MASS)
SIZE = 2 * m + 1
MIN_ITEM = -100
MAX_ITEM = 200
arr = [random.randint(MIN_ITEM, MAX_ITEM // 2) for _ in range(SIZE)]

print(arr)
for i, item_i in enumerate(arr):
    i_less = 0
    i_more = 0
    i_equally = 0

    for j, item_j in enumerate(arr):
        if j != i:
            if item_i == item_j:
                i_equally += 1
            if item_i < item_j:
                i_less += 1
            if item_i > item_j:
                i_more += 1

    if len(arr) - (i_less + i_equally + 1) <= len(arr) // 2 and i_more + i_equally + 1 > len(arr) // 2:
        median = item_i

# print(arr)
print('Медиана! =', median)
print('Проверка =', statistics.median(arr))
