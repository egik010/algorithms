# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

object_company = namedtuple('object_company',
                                        ['quarter1', 'quarter2', 'quarter3', 'quarter4', 'for_year'],
                                        defaults='0')
sum_for_year = 0
company = {}
num_company = int(input("Введите количество предприятий: "))
for i in range(num_company):
    name_company = input(f' Введите имя предприятия {i + 1}: ')
    q1 = int(input('Введите прибыль за 1 квартал: '))
    q2 = int(input('Введите прибыль за 2 квартал: '))
    q3 = int(input('Введите прибыль за 3 квартал: '))
    q4 = int(input('Введите прибыль за 4 квартал: '))
    company[name_company] = object_company(
        quarter1=q1,
        quarter2=q2,
        quarter3=q3,
        quarter4=q4,
        for_year=q1 + q2 + q3 + q4  # можно было бы потом или sum или отдельным циклом посчитать
    )
    sum_for_year += company[name_company].for_year

avr_for_year = sum_for_year / len(company)
print(f'Средняя прибыль всех {len(company)} предприятий = {avr_for_year}')

print('Предприятия, что заработали больше среднего по всем препедприятиям:')
for i in company:
    if company[i].for_year >= avr_for_year:
        print(f'Предприятие {i}, заработало за год {company[i].for_year}')

print('Предприятия, что заработали меньше среднего по всем препедприятиям:')
for i in company:
    if company[i].for_year < avr_for_year:
        print(f'Предприятие {i}, заработало за год {company[i].for_year}')
