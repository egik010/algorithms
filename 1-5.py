# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
# a - 97 ,  z - 122

a1 = input('Введите первую букву из диапазона a-z: ')
a2 = input('Введите вторую букву из диапазона a-z: ')

a1_pos = ord(a1) - 96
a2_pos = ord(a2) - 96
a1_a2_delta = abs(a1_pos - a2_pos) - 1

print('Порядковый номер первой буквы:', a1_pos)
print('Порядковый номер второй буквы:', a2_pos)
print('Количество букв между введенными буквами:', a1_a2_delta)
