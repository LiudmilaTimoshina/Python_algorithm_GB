# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
# использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной
# и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях
# версию Python и разрядность вашей ОС.


import sys
import random

def my_decor(func, args):
    def objects(args):
        func(args)
        return locals()

    return objects(args)

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)


# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

def max_min_list(num_list):
    print(num_list)
    min_idx = num_list.index(min(num_list))
    max_idx = num_list.index(max(num_list))
    if max_idx < min_idx:
        max_idx, min_idx = min_idx, max_idx
    num_list_short = num_list[min_idx + 1: max_idx]
    num_list_sum = 0
    for num_el in num_list_short:
        num_list_sum += num_el
    print(f'Элементы между максимальным и минимальным {num_list_short} '
          f'\nСумма элементов, находящихся между минимальным и максимальным элементом, равна {num_list_sum}')
    return locals()

#num_list = [random.randint(0, 100) for _ in range(20)]
#show_size(max_min_list(num_list))

'''
[76, 50, 98, 21, 19, 83, 92, 29, 10, 57, 44, 56, 38, 19, 29, 15, 13, 41, 18, 76]
Элементы между максимальным и минимальным [21, 19, 83, 92, 29] 
Сумма элементов, находящихся между минимальным и максимальным элементом, равна 244
 type = <class 'dict'>, size = 360, object = {'num_list': [76, 50, 98, 21, 19, 83, 92, 29, 10, 57, 44, 56, 38, 19, 29, 15, 13, 41, 18, 76], 'min_idx': 2, 'max_idx': 8, 'num_list_short': [21, 19, 83, 92, 29], 'num_list_sum': 244, 'num_el': 29}
	 type = <class 'tuple'>, size = 56, object = ('num_list', [76, 50, 98, 21, 19, 83, 92, 29, 10, 57, 44, 56, 38, 19, 29, 15, 13, 41, 18, 76])
		 type = <class 'str'>, size = 57, object = num_list
		 type = <class 'list'>, size = 248, object = [76, 50, 98, 21, 19, 83, 92, 29, 10, 57, 44, 56, 38, 19, 29, 15, 13, 41, 18, 76]
			 type = <class 'int'>, size = 28, object = 76
			 type = <class 'int'>, size = 28, object = 50
			 type = <class 'int'>, size = 28, object = 98
			 type = <class 'int'>, size = 28, object = 21
			 type = <class 'int'>, size = 28, object = 19
			 type = <class 'int'>, size = 28, object = 83
			 type = <class 'int'>, size = 28, object = 92
			 type = <class 'int'>, size = 28, object = 29
			 type = <class 'int'>, size = 28, object = 10
			 type = <class 'int'>, size = 28, object = 57
			 type = <class 'int'>, size = 28, object = 44
			 type = <class 'int'>, size = 28, object = 56
			 type = <class 'int'>, size = 28, object = 38
			 type = <class 'int'>, size = 28, object = 19
			 type = <class 'int'>, size = 28, object = 29
			 type = <class 'int'>, size = 28, object = 15
			 type = <class 'int'>, size = 28, object = 13
			 type = <class 'int'>, size = 28, object = 41
			 type = <class 'int'>, size = 28, object = 18
			 type = <class 'int'>, size = 28, object = 76
	 type = <class 'tuple'>, size = 56, object = ('min_idx', 2)
		 type = <class 'str'>, size = 56, object = min_idx
		 type = <class 'int'>, size = 28, object = 2
	 type = <class 'tuple'>, size = 56, object = ('max_idx', 8)
		 type = <class 'str'>, size = 56, object = max_idx
		 type = <class 'int'>, size = 28, object = 8
	 type = <class 'tuple'>, size = 56, object = ('num_list_short', [21, 19, 83, 92, 29])
		 type = <class 'str'>, size = 63, object = num_list_short
		 type = <class 'list'>, size = 96, object = [21, 19, 83, 92, 29]
			 type = <class 'int'>, size = 28, object = 21
			 type = <class 'int'>, size = 28, object = 19
			 type = <class 'int'>, size = 28, object = 83
			 type = <class 'int'>, size = 28, object = 92
			 type = <class 'int'>, size = 28, object = 29
	 type = <class 'tuple'>, size = 56, object = ('num_list_sum', 244)
		 type = <class 'str'>, size = 61, object = num_list_sum
		 type = <class 'int'>, size = 28, object = 244
	 type = <class 'tuple'>, size = 56, object = ('num_el', 29)
		 type = <class 'str'>, size = 55, object = num_el
		 type = <class 'int'>, size = 28, object = 29
'''


# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def max_sum_num(num_list_2):
    max_sum = 0
    for i in num_list_2:
        digit_sum = 0
        n = i
        while i % 10 != 0 or i // 10 != 0:
            digit_sum += i % 10
            i //= 10
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = n
    print(f'У числа {max_num} наибольшая сумма цифр  {max_sum}')
    return locals()

#num_list_2 = [random.randint(100, 999) for _ in range(20)]
#show_size(max_sum_num(num_list_2))

'''
У числа 998 наибольшая сумма цифр = 26
 type = <class 'dict'>, size = 360, object = {'num_list_2': [998, 351, 748, 589, 789, 642, 712, 962, 486, 115, 524, 148, 752, 549, 478, 989, 222, 233, 505, 322], 'max_sum': 26, 'i': 0, 'digit_sum': 7, 'n': 322, 'max_num': 998}
	 type = <class 'tuple'>, size = 56, object = ('num_list_2', [998, 351, 748, 589, 789, 642, 712, 962, 486, 115, 524, 148, 752, 549, 478, 989, 222, 233, 505, 322])
		 type = <class 'str'>, size = 59, object = num_list_2
		 type = <class 'list'>, size = 248, object = [998, 351, 748, 589, 789, 642, 712, 962, 486, 115, 524, 148, 752, 549, 478, 989, 222, 233, 505, 322]
			 type = <class 'int'>, size = 28, object = 998
			 type = <class 'int'>, size = 28, object = 351
			 type = <class 'int'>, size = 28, object = 748
			 type = <class 'int'>, size = 28, object = 589
			 type = <class 'int'>, size = 28, object = 789
			 type = <class 'int'>, size = 28, object = 642
			 type = <class 'int'>, size = 28, object = 712
			 type = <class 'int'>, size = 28, object = 962
			 type = <class 'int'>, size = 28, object = 486
			 type = <class 'int'>, size = 28, object = 115
			 type = <class 'int'>, size = 28, object = 524
			 type = <class 'int'>, size = 28, object = 148
			 type = <class 'int'>, size = 28, object = 752
			 type = <class 'int'>, size = 28, object = 549
			 type = <class 'int'>, size = 28, object = 478
			 type = <class 'int'>, size = 28, object = 989
			 type = <class 'int'>, size = 28, object = 222
			 type = <class 'int'>, size = 28, object = 233
			 type = <class 'int'>, size = 28, object = 505
			 type = <class 'int'>, size = 28, object = 322
	 type = <class 'tuple'>, size = 56, object = ('max_sum', 26)
		 type = <class 'str'>, size = 56, object = max_sum
		 type = <class 'int'>, size = 28, object = 26
	 type = <class 'tuple'>, size = 56, object = ('i', 0)
		 type = <class 'str'>, size = 50, object = i
		 type = <class 'int'>, size = 24, object = 0
	 type = <class 'tuple'>, size = 56, object = ('digit_sum', 7)
		 type = <class 'str'>, size = 58, object = digit_sum
		 type = <class 'int'>, size = 28, object = 7
	 type = <class 'tuple'>, size = 56, object = ('n', 322)
		 type = <class 'str'>, size = 50, object = n
		 type = <class 'int'>, size = 28, object = 322
	 type = <class 'tuple'>, size = 56, object = ('max_num', 998)
		 type = <class 'str'>, size = 56, object = max_num
		 type = <class 'int'>, size = 28, object = 998
'''
#PyCharm 2021.2.3 (Community Edition)
#Runtime version: 11.0.12+7-b1504.40 amd64sd
#64-разрядная операционная система, процессор x64


