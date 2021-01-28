# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

# 5 строк и 4 столбца
import random  #для тестов - 19 строка

C = 4  # столбцы
R = 5  # строк

matrix = []
for i in range(R):  # по строкам
    a = []
    z = 0
    for j in range(C):  # по столбцам
        if j == C - 1:
            a.append(z)
        else:
            #v = random.randint(0, 10)
            v = int(input(f'Введите число {i + 1} строки и {j + 1} столбца: '))
            z += v
            a.append(v)
    matrix.append(a)

for line in matrix:
    for i in line:
        print(f'{i:>6}', end='')
    print()
