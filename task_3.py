# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

num_list = [random.randint(0, 100) for _ in range(10)]
print(f'Исходный список:\n{num_list}')
max_el = max(num_list)
max_idx = num_list.index(max(num_list))
min_el = min(num_list)
min_idx = num_list.index(min_el)
num_list[min_idx] = max_el
num_list[max_idx] = min_el
print('Список, в котором изменены местами максимальный и минимальный элементы:\n', num_list)