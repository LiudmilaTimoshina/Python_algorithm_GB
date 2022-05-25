# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

ans = 0

while True:
    num1, num2 = map(int, input('Введите два числа через пробел: ').split())
    while True:
        op = input('Введите знак операции +, -, *, / или 0 для завершения операции: ')
        if op == '0':
            break
        elif op == '+':
            ans = num1 + num2
            print(f'{num1} {op} {num2} = {ans}')
        elif op == '-':
            ans = num1 - num2
            print(f'{num1} {op} {num2} = {ans}')
        elif op == '*':
            ans = num1 * num2
            print(f'{num1} {op} {num2} = {ans}')
        elif op == '/':
            if num2 == 0:
                print('На ноль делить нельзя')
                break
            else:
                ans = num1 / num2
                print(f'{num1} {op} {num2} = {ans}')
        else:
            print('Неверный формат ввода. Попробуйте еще раз!')