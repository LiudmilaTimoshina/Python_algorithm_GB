# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_sum = 0
while True:
    num = int(input('Введите целое число. Для завершения ввода чисел укажите "0": '))
    if num == 0:
        break
    digit_sum = 0
    n = num
    while num % 10 != 0 or num // 10 != 0:
        digit_sum += num % 10
        num //= 10
    if digit_sum > max_sum:
        max_sum = digit_sum
        max_num = n
print(f'У числа {max_num} наибольшая сумма цифр. Эта сумма равна {max_sum}')

