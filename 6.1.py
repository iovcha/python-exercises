#7. Найти периметр многоугольника
from math import sqrt
x1 = float(input("Введите первую координату X: "))
y1 = float(input("Введите первую координату Y: "))
prev_x = float(x1)
prev_y = float(y1)
line = input("Введите следующую координату X: ")
perimeter = 0
while line != '':
    x = float(line)
    y = float(input("Введите следующую координату Y:"))
    d = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter += d
    prev_x = x
    prev_y = y
    line = input("Введите следующую координату X: ")
d = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
perimeter += d
print("Периметр многоугольника равен %.2f." % perimeter)




