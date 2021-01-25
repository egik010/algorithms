# 5. Вывести на экран коды и символы таблицы ASCII, начиная
# с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

BEGIN_ASCII = 32
END_ASCII = 127

i = BEGIN_ASCII
new_str = 1
while i <= END_ASCII:
    print(F'{i}-"{chr(i)}" ', end=" ")
    if new_str == 10:
        print('\n')
        new_str = 0
    i += 1
    new_str += 1
