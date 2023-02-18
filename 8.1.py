#Тема 1: “Ветвления”
#11.	Дана точка M с координатами (x, y). Определить месторасположение этой точки в декартовой системе координат:
#a.	является началом координат
#b.	лежит на одной из координатных осей
#c.	расположена в одном из координатных углов

#x = int(input('Введите координаты точки по ОХ: '))
#y = int(input('Введите координаты точки по ОY: '))

#if x == 0 and y == 0:
#    m = 'является началом координат'
#elif x == 0 and y < 0 or y > 0:
#    m = 'лежит на одной из координатных осей'
#elif y == 0 and x < 0 or x > 0:
   # m = 'лежит на одной из координатных осей'
#else:
   # m = 'расположена в одном из координатных углов'
#print(m)

#22.	Выяснить, пересекаются ли параболы y = ax2 + bx + c и y = dx2 + ex + f. Если да, найти точки пересечения.
#import math
#a = float(input('Введите число не равное 0:'))
#b = float(input('Введите число :'))
#c = float(input('Введите число :'))
#d = float(input('Введите число не равное 0:'))
#e = float(input('Введите число :'))
#f = float(input('Введите число :'))
#t = a - d
#j = b - e
#n = c - f
#discr = j ** 2 - 4 * t * n
#print("Дискриминант D = %.2f" % discr)
#if discr > 0:
#    x1 = (-j + math.sqrt(discr)) / (2 * t)
#    x2 = (-j - math.sqrt(discr)) / (2 * t)
#    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
#    y1 = a * x1 ** 2 + b * x1 + c
#    y2 = a * x2 ** 2 + b * x2 + c
#    print("Точки пересечения парабол x1 = %.2f \ny1 = %.2f" % (x1, y1))
#    print("Точки пересечения парабол x2 = %.2f \ny2 = %.2f" % (x2, y2))
#elif discr == 0:
#    x = -j / (2 * t)
#    print("x = %.2f" % x)
#    y = a * x ** 2 + b * x + c
#    print("Точки пересечения парабол x = %.2f \ny = %.2f" % (x, y))
#else:
#    print("Корней нет")
#    print("Парпболы не пересекаются")

#3.	Дан массив целых чисел. Найти его минимальный и максимальный элементы.
#Если минимальный элемент расположен раньше максимального, найти среднее арифметическое всех элементов между ними,
#а если после - заменить данные элементы на их среднее геометрическое.
import math
line = input('Введите число : ')
sp = []
while line != "":
    i = int(line)
    sp.append(i)
    line = input('Введите число : ')
max_elm = max(sp)
min_elm = min(sp)
print(sp, "Максимальный элемент = ", max_elm ,"Минимальный элемент = ", min_elm)
if sp.index(max(sp)) > sp.index(min(sp)):
    arith_mean = (sum(sp[min(sp.index(min_elm), sp.index(max_elm)) + 1:max(sp.index(min_elm), sp.index(max_elm))])) / \
    len(sp[min(sp.index(min_elm), sp.index(max_elm)) + 1:max(sp.index(min_elm), sp.index(max_elm))])
    if sum(sp[min(sp.index(min_elm), sp.index(max_elm)) + 1:max(sp.index(min_elm), sp.index(max_elm))]) == 0:
        print("Cреднее арифметическое всех элементов между минимальным и максимальным элементом = 0")
    else:
        print("Cреднее арифметическое всех элементов между минимальным и максимальным элементом", arith_mean)
elif sp.index(max(sp)) < sp.index(min(sp)):
    n = len(sp[min(sp.index(min_elm), sp.index(max_elm)) + 1:max(sp.index(min_elm), sp.index(max_elm))])
    l = sp[min(sp.index(min_elm), sp.index(max_elm)) + 1:max(sp.index(min_elm), sp.index(max_elm))]
    l_new = [i for i in l if i != 0]
    n_new = len(l_new)
    p = abs(math.prod(l_new))
    geon_min = (math.sqrt(p) ** (1 / n_new))
    print("Cреднее геометрическое всех элементов между максимальным и минимальным  %.2f." % geon_min)
    del sp[min(sp.index(min_elm), sp.index(max_elm)) + 1:max(sp.index(min_elm), sp.index(max_elm))]
    m = sp.index(max_elm) + 1
    sp.insert(m, round(geon_min, 2))
    print(sp)












