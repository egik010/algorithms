# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные
# (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
# остальные годы, номер которых кратен 4, — високосные.

my_year = int(input('Введите год (число от 1000 до 2020) : '))

if (my_year % 400 == 0) or (my_year % 100 != 0) and (my_year % 4 == 0):
    print(F'{my_year} год является високосным')
else:
    print(F'{my_year} год не является високосным')
