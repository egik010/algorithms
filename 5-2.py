# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой —
# цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque

number1 = deque(input('Введите 1 число буквы анг и только в верхнем регистре: '))
number2 = deque(input('Введите 2 число буквы анг и только в верхнем регистре: '))
# number1 = deque(['A', '2'])
# number2 = deque(['C', '4', 'F'])

dec_hex = {x: str(x) for x in range(0, 16)}
dec_hex[10], dec_hex[11], dec_hex[12], dec_hex[13], dec_hex[14], dec_hex[15] = 'A', 'B', 'C', 'D', 'E', 'F'

# hex_dec = {j: i for i, j in dec_hex.items()}  # поменяем ключи и значения в новом списке
hex_dec = dict(reversed(item) for item in dec_hex.items())

# выровняем длину обоих
if len(number1) < len(number2):
    for _ in range(len(number2) - len(number1)):
        number1.appendleft('0')

if len(number2) < len(number1):
    for _ in range(len(number1) - len(number2)):
        number2.appendleft('0')

# добавим в начало 0 так как может 1 перенестись
number1.appendleft('0')
number2.appendleft('0')
number1.reverse()
number2.reverse()

d = 0
number12 = deque()
for i in range(len(number1)):
    sum12 = hex_dec[number1[i]] + hex_dec[number2[i]] + d
    if sum12 <= 9:
        number12.append(str(sum12))
        d = 0
    if 9 < sum12 <= 15:
        number12.append(dec_hex[sum12])
        d = 0
    if sum12 > 15:
        number12.append(dec_hex[sum12 - 16])
        d = 1

number12.reverse()
# удалим 0
for i in range(len(number12)):
    if number12[i] == '0':
        number12.popleft()
    else:
        break

print('Cумма: ', number12)
