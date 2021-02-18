# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9

def number_of_substrings(my_str):
    count_of_substrings = set()
    for sub_str in range(len(my_str)):
        for delta in range(1, len(my_str)):
            count_of_substrings.add(hash(my_str[sub_str:sub_str + delta]))

    return len(count_of_substrings)


# s = 'abab'
# s = 'papa'
# s = 'sova'
s = input('Введите строку из букв: ')
print(number_of_substrings(s))
