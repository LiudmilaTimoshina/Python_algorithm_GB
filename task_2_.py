#2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# Вариант 1. Решето Эратосфена.
import time

begin = time.perf_counter()
a = [i for i in range(101)]
print(a)
a[1] = 0
m = 2
while m < len(a):
    if m!=0:
        j = m*2
        while j < len(a):
            a[j] = 0
            j += m
    m += 1
b = [i for i in a if i > 1]
print(b)
print('time = ', time.perf_counter() - begin)

# time
# 0.0002239999594166875    [i for i in range(101)]
# 6.19000056758523e-05     [i for i in range(11)]
# 0.012834000051952899     [i for i in range(1001)]

# Вариант 2. Перебор.

begin = time.perf_counter()
a = [i for i in range(101)]
print(a)
a[1] = 0
for i in range(2, len(a)):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(i)
b = [i for i in a if i > 1]
print(b)
print('time = ', time.perf_counter() - begin)