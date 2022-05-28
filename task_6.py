# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

num_list = [random.randint(0, 10) for _ in range(10)]
print(f'Массив чисел {num_list}')
min_idx = num_list.index(min(num_list))
max_idx = num_list.index(max(num_list))
if max_idx < min_idx:
    max_idx, min_idx = min_idx, max_idx
num_list_short = num_list[min_idx + 1 : max_idx]
num_list_sum = 0
for num_el in num_list_short:
    num_list_sum += num_el
print(f'Элементы между максимальным и минимальным {num_list_short} \nСумма элементов, находящихся между минимальным и максимальным элементом, равна {num_list_sum}')