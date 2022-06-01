# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне
# от 2 до 9.

div_dict = dict.fromkeys(range(2, 10), 0)
num_list = [i for i in range(2, 100)]
print(f'Исходный диапазон чисел от 2 до 99:\n{num_list}')
for num in num_list:
    for i in range(2, 10):
        if num % i == 0:
            div_dict[i] += 1
for key in div_dict:
    print(f'Числу {key} кратны {div_dict[key]} чисел из массива')