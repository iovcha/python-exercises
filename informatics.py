##12 Дачники
from math import sqrt


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


