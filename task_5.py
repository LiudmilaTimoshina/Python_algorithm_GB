# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

num_list = [random.randint(-10, 10) for _ in range(10)]
num_list_short = [i for i in num_list if i < 0]
max = max(num_list_short)
print(f'В массиве {num_list} максимальный отрицательный элемент {max}')