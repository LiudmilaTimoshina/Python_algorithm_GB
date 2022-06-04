# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.


import collections

n = int(input('Введите количество компаний: '))
companies = collections.defaultdict()
prof_c = collections.deque()
unprof_c = collections.deque()
profit_total = 0
for i in range(n):
    name = input(f'Введите название {i+1}й компании: ')
    profit = 0
    profit_quarter = list(map(float, (input(f'Введите прибыль компании за 4 квартала через пробел: ').split())))
    profit_year = sum(profit_quarter)
    companies[name] = profit_year
    profit_total += profit_year
mid_profit = profit_total / n
print(mid_profit)
for i, item in companies.items():
    if item >= mid_profit:
        prof_c.append(i)
    else:
        unprof_c.append(i)
print(f'Средняя прибыль для всех компаний: {mid_profit}')
print(f'Прибыль выше среднего у {len(prof_c)} компаний:')
for name in prof_c:
    print(name)
print(f'Прибыль ниже среднего у {len(unprof_c)} компаний:')
for name in unprof_c:
    print(name)
