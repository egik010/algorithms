# 1). Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# выбрал 4 задачу из 3 домашнего задания
# Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import cProfile

SIZE = 5000
MIN_ITEM = 0
MAX_ITEM = 20
arr = [random.randint(MIN_ITEM, MAX_ITEM / 2) for _ in range(SIZE)]

#print(arr)


def my_max_mem(array):
    # переберем ммассив и создадим словарь, в котором ключ это элемент массива, а значение - количество вхождений
    d = {}
    for line in array:
        if line not in d.keys():
            d[line] = 1
        else:
            d[line] = d[line] + 1
    # print(d)

    # теперь найдет в словаре максимальное количество вхождений
    max_ar = 0
    max_num = 0
    for i in d:
        if max_ar < d[i]:
            max_ar = d[i]
            max_num = i
    return max_num


def my_max_for(array):  # сделаем двойным for
    num = arr[0]
    max_frq = 1
    for i in range(len(array) - 1):
        frq = 1
        for k in range(i + 1, len(array)):
            if arr[i] == arr[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]
    return num


def my_max_count(array):  # используем функцию count
    num = arr[0]
    max_frq = 1
    for i in range(len(array) - 1):
        if array.count(array[i]) > max_frq:
            max_frq = array.count(array[i])
            num = array[i]
    return num


# будем проверять на одном случайном массиве,для  это этого последовательно
# меняя SIZE сделаем замеры на разных длинах массива чтобы определить закономерность
# #SIZE = 100
# print(timeit.timeit('my_max_mem(arr)', number=100, globals=globals()))   # 0.002364738000000005
# print(timeit.timeit('my_max_for(arr)', number=100, globals=globals()))   # 0.070546398
# print(timeit.timeit('my_max_count(arr)', number=100, globals=globals())) # 0.020068877999999984

# #SIZE = 200
# print(timeit.timeit('my_max_mem(arr)', number=100, globals=globals()))   # 0.004389284
# print(timeit.timeit('my_max_for(arr)', number=100, globals=globals()))   # 0.28851611099999996
# print(timeit.timeit('my_max_count(arr)', number=100, globals=globals())) # 0.07597195300000004

# #SIZE = 300
# print(timeit.timeit('my_max_mem(arr)', number=100, globals=globals()))    # 0.006738024000000002
# print(timeit.timeit('my_max_for(arr)', number=100, globals=globals()))    # 0.626299904
# print(timeit.timeit('my_max_count(arr)', number=100, globals=globals()))  # 0.1713945819999999

# #SIZE = 400
# print(timeit.timeit('my_max_mem(arr)', number=100, globals=globals()))      # 0.008671710999999999
# print(timeit.timeit('my_max_for(arr)', number=100, globals=globals()))      # 1.168575853
# print(timeit.timeit('my_max_count(arr)', number=100, globals=globals()))    # 0.311488236

# SIZE = 5000
cProfile.run('my_max_mem(arr)')
cProfile.run('my_max_for(arr)')
cProfile.run('my_max_count(arr)')

# ВЫВОДЫ:
# Как и в задумке первый вариант с использование дополнтительного словаря
# самый быстрый
# Вложенные циклы самые меделенные
# Сложность O(n) - линейная сложность
