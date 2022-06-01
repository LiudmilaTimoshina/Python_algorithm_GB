#1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках
# домашнего задания первых трех уроков.

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import time

begin = time.perf_counter()
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
print(f'Элементы между максимальным и минимальным {num_list_short} '
      f'\nСумма элементов, находящихся между минимальным и максимальным элементом, равна {num_list_sum}')
print('time = ', time.perf_counter() - begin)

#   time
#   8.679996244609356e-05   [random.randint(0, 10) for _ in range(10)]
#   0.00012830004561692476  [random.randint(0, 100) for _ in range(10)]
#   0.000255799968726933    [random.randint(0, 10) for _ in range(100)]

begin = time.perf_counter()
num_list = [random.randint(0, 10) for _ in range(10)]
print(f'Массив чисел {num_list}')
min_el = num_list[0]
max_el = num_list[1]
for i, item in enumerate(num_list):
    if item <= min_el:
        min_el = item
        min_idx = i
    if item >= max_el:
        max_el = item
        max_idx = i
if max_idx < min_idx:
    max_idx, min_idx = min_idx, max_idx
num_list_sum = 0
for num_el in num_list_short:
    num_list_sum += num_el
print(f'Элементы между максимальным и минимальным {num_list_short} '
      f'\nСумма элементов, находящихся между минимальным и максимальным элементом, равна {num_list_sum}')
print('time = ', time.perf_counter() - begin)

# time
# 4.75000124424696e-05  [random.randint(0, 10) for _ in range(10)]
