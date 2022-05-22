# 4. Написать программу, которая генерирует в указанных пользователем границах:
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.
#     Для каждого из трех случаев пользователь задает свои границы диапазона.
#     Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
#     Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

x1, x2 = map(int, input('Введите границы для случайного целого числа: ').split())
y1, y2 = map(float, input('Введите границы для случайного вещественного числа: ').split())
ch1, ch2 = input('Введите границы для случайной буквы: ').split()

r_int = random.randint(x1, x2)
r_float = random.uniform(y1, y2)
r_char = chr(random.randint(ord(ch1), ord(ch2)))

print(f'Случайное целое число: {r_int}\n'
      f'Случайное вещественное число: {r_float}\n'
      f'Случайная буква: "{r_char}"')