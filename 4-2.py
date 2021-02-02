# 2). Написать два алгоритма нахождения i-го по счёту простого числа.
#     Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число.
#     Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
#     Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import timeit
import cProfile


def prime_number_er(my_index, n):
    # n = 2000
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    sieve = [i for i in sieve if i != 0]
    return sieve[my_index - 1]


def prime_number(n):
    num = 1
    j = 0
    while True:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                j += 1
        if j == n:
            break
        num += 1
    return num


print(timeit.timeit('prime_number_er(300, 2000)', number=100, globals=globals())) #0.10598516499999999
print(timeit.timeit('prime_number(300)', number=100, globals=globals()))          #2.152342053

cProfile.run('prime_number_er(300, 2000)')
cProfile.run('prime_number(300)')

# ВЫВОДЫ
# Наглядно видно насколько решето Эратосфена работает быстрее
