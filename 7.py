#1.	Вычислить сумму натуральных четных чисел, не превышающих N.
#n = int(input("введите число: "))
#summa = 0
#for x in range(1, (n + 1)):
#    if x % 2 == 0:
#        print(x)
#        summa += x
#print(summa)

#2.	Дано натуральное число N. Определить, является ли оно простым.
#n = int(input("введите число для определения: "))
#k = 0
#for i in range(2, (n // 2) + 1 ):
#    if n % i == 0:
#        k += 1
#if k <= 0:
#    print(" простое число")
#else:
#     print("Не простое число")

#3.	Дана последовательность целых положительных чисел. Определить количество простых чисел в последовательности
#l = [6,  8, 9, 14, 7, 38, 40, 1, 11, 13, 76, 31, 111, 34]
#l. remove(1)#удалим 1 , так как она и не простое и не сложное число
#count = len(l)
#for i in l:
#    for j in range(2, (i // 2) + 1):
#        if i % j == 0:#находим все не простые числа
#            count -= 1
#            break
#if count == 0:
#    print("Простых чисел нет")
#else:
#    print("Колличество простых чисел = ", count)

#4.	Дана последовательность целых чисел. Найти наименьшее число среди положительных элементов последовательности.
# Если присутствует несколько одинаковых наименьших элементов, то определить их количество.
l = [4, 8, 1, 2, 16, -10, 2, 15, -100, 9, 7, 0, -5, 1, 1, 1, 1]
l.sort(reverse=True)#если последовательность начинается с отрицательного числа
el_min = l[0]
k = 0
for i in l:
    if i > 0 and i < el_min:
        el_min = i
        k = 1
    elif i > 0 and i == el_min:
        k += 1
if k == 0:
    print('Положительных чисел нет')
else:
    print('Последовательность содержит', k,'минимальных элемента')



























