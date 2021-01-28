# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE_N = 3  # столбцы
SIZE_M = 4
MIN_ITEM = 0
MAX_ITEM = 10
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]

# сделаем одномерный массив с минимальными значениями столбцов
# m_min_n = []
for i, line in enumerate(matrix):
    if i == 0:
        m_min_n = line
    for j, item in enumerate(line):
        print(f'{item:>6}', end='')
        if m_min_n[j] > item:
            m_min_n[j] = item
    print()

#print(m_min_n)

#найдем максимум в нашем массиве минимумов
max_min = 0
for i in m_min_n:
    if max_min < i:
        max_min = i

print(f'Число {max_min} максимальный элемент среди минимальных элементов столбцов матрицы')
