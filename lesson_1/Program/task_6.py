# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы в латинском алфавите от 1 до 26: '))

char = chr(num + 64)

print(f'Номеру {num} в алфавите соотвествует буква "{char}"')