#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’].
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
a, b = input('Введите числа в шестнадцатеричной системе через проблел: ').split()

hex_sum = hex(int(a, 16) + int(b, 16))
hex_multi = hex(int(a, 16) * int(b, 16))
print(f'Сумма чисел: {hex_sum[2:].upper()}')
print(f'Произведение чисел: {hex_multi[2:].upper()}')
"""

import collections
from copy import deepcopy

hex_str = '0123456789ABCDEF'
hex_tbl = collections.defaultdict(int)
int_tbl = collections.defaultdict(int)
for i, item in enumerate(hex_str):
    hex_tbl[item] = i
    int_tbl[i] = item


class HexNum:
    h_tbl = hex_tbl
    i_tbl = int_tbl

    def __init__(self, num):
        self.num = collections.deque()
        for item in num:
            self.num.append(item.upper())

    def __str__(self):
        s = ''
        for i in self.num:
            s += i
        return s

    def __add__(self, other):
        if len(other.num) > len(self.num):
            a = deepcopy(other.num)
            b = deepcopy(self.num)
        else:
            a = deepcopy(self.num)
            b = deepcopy(other.num)
        temp = 0
        result = collections.deque()
        for i in range(len(a)):
            first = self.h_tbl[a.pop()]
            if len(b) != 0:
                second = self.h_tbl[b.pop()]
            else:
                second = 0
            temp_res = first + second + temp
            if temp_res > 15:
                temp = 1
            else:
                temp = 0
            temp_res %= 16
            result.appendleft(self.i_tbl[temp_res])
        if temp != 0:
            result.appendleft(self.i_tbl[temp])
        result = HexNum(result)
        return result

    def __mul__(self, other):
        a = deepcopy(self.num)
        b = deepcopy(other.num)
        dec = 0
        answer = HexNum('0')
        result = collections.deque()
        for i in range(len(a) - 1, -1, -1):
            temp = 0
            for j in range(len(b) - 1, -1, -1):
                temp_res = self.h_tbl[a[i]] * self.h_tbl[b[j]] + temp
                if temp_res > 15:
                    temp = temp_res // 16
                else:
                    temp = 0
                temp_res = temp_res % 16
                result.appendleft(self.i_tbl[temp_res % 16])
            if temp != 0:
                result.appendleft(self.i_tbl[temp])
            for d in range(dec):
                result.append('0')
            result = HexNum(result)
            answer += result
            result = collections.deque()
            dec += 1
        return answer


a = HexNum('a2')
b = HexNum('C4F')

print(a + b)
print(a * b)