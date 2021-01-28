# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE_N = 3 #столбцы
SIZE_M = 4
MIN_ITEM = 0
MAX_ITEM = 10
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]

for line in matrix:
    for i in line:
        print(f'{i:>6}', end='')
    print()

print()
# Вариант с перебором по столбцам по индексам,
# только на знаю транспонирование все же это или нет

max_min = 0
for line in range(SIZE_N):
    min_n = matrix[0][line]
    for i in range(SIZE_M):
        if matrix[i][line] < min_n:
            min_m = matrix[i][line]
    if max_min < min_n:
        max_min = min_n

print(f'Число {max_min} максимальный элемент среди минимальных элементов столбцов матрицы')