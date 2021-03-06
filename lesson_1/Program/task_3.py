# По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y=kx+b, проходящей через эти точки.

x1, y1 = map(float, input('Введите координаты первой точки (x1, y1): ').split())
x2, y2 = map(float, input('Введите координаты второй точки (x2, y2): ').split())

k = (y1 - y2) / (x2 - x1)
b = y2 - (k * x2)

print(f'Уравнение прямой: y = {k}x + {b}')