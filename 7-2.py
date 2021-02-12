# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50


def sort_merge(arr):
    if len(arr) <= 1:
        return arr

    arr1 = sort_merge(arr[:len(arr) // 2])
    arr2 = sort_merge(arr[len(arr) // 2:])
    i = 0
    j = 0
    while len(arr1) > i and len(arr2) > j:
        if arr1[i] < arr2[j]:
            arr[i + j] = arr1[i]
            i += 1
        else:
            arr[i + j] = arr2[j]
            j += 1

    while len(arr1) > i:
        arr[i + j] = arr1[i]
        i += 1
    while len(arr2) > j:
        arr[i + j] = arr2[j]
        j += 1
    return arr


my_array = [random.randint(MIN_ITEM, MAX_ITEM // 2) for _ in range(SIZE)]

print('Исходный массив            :', my_array)
print('Проверочный массив (sorted):', sorted(my_array))
print('Массив после сортировки    :', sort_merge(my_array))
