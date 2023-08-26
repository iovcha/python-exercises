##12 Дачники
from math import sqrt
from time import time
stt = time()


def sq(ax, ay, bx, by, cx, cy):
    """площадь триуголника, косого произведения векторов
    где ax, ay, bx, by, cx, cy координаты точек """
    return abs((ax - bx) * (cy - by) - (ay - by) * (cx - bx))


count = 0
for i in range(int(input())):
    ox, oy, ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
    s = sq(ax, ay, bx, by, cx, cy) + sq(ax, ay, dx, dy, cx, cy)
    s1 = sq(ax, ay, bx, by, ox, oy)
    s2 = sq(cx, cy, bx, by, ox, oy)
    s3 = sq(ax, ay, dx, dy, ox, oy)
    s4 = sq(cx, cy, dx, dy, ox, oy)
    if s == s1 + s2 + s3 + s4:
        count += 1
print(count)
print(time()-stt)

#####2
##Задано натуральное число N. Требуется написать программу,
# вычисляющую количество различных трехзначных чисел получающихся из N вычеркиванием цифр из его десятичной записи.


from time import time
stt = time()
s = input()
A = set()
for i in range(len(s)):
    for j in range(i+1, len(s)):
        for k in range(j+1, len(s)):
            a = int(''.join((s[i], s[j], s[k])))
            if a >= 100:
                A.add(a)
print(len(A))
print(time()-stt)
