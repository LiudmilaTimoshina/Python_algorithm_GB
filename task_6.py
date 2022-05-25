# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.

import random

number = random.randint(0, 101)
for i in range(10):
    num = int(input('Угадайте целое число от 0 до 100: '))
    if num == number:
        print('Поздравляю! Вы угадали!')
        break
    elif num < number:
        print('Ваше число меньше загаданного. Попробуйте еще раз!')
    else:
        print('Ваше число больше загаданного. Попробуйте еще раз!')
print(f'Было загадано число {number}')