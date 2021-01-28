# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# переберем ммассив и создадим словарь, в котором ключ это элемент массива, а значение - количество вхождений
d = {}
for i, line in enumerate(array):
    if line not in d.keys():
        d[line] = 1
    else:
        d[line] = d[line] + 1
print(d)

# теперь найдет в словаре максимальное количество вхождений
max_ar = 0
max_num = 0
for i in d:
    if max_ar < d[i]:
        max_ar = d[i]
        max_num = i

print(f'Число которое чаще всего встречается в массиве {max_num}, количество вхождений {max_ar}')
