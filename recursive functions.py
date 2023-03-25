#1.	Написать рекурсивную функцию подсчета суммы элементов списка чисел.

#def sum_arr(arr, size):#size длинна списка
#    if (size == 0):
#        return 0
#    else:
#        return arr[size - 1] + sum_arr(arr, size - 1)
#n = int(input("Введите длину списка:"))
#a = []
#for i in range(0, n):
#    element = int(input("Введите элемент списка:"))
#    a.append(element)
#print("Весь список:")
#print(a)
#print("Сумма элементов списка равна:")
#b = sum_arr(a, n)
#print(b)

#2.	Написать рекурсивную функцию подсчета суммы цифр положительного целого числа.

#l = []
#def sum_digit(num):
#    if num == 0:
#        return l
#    dig = num % 10
#    l.append(dig)
#    sum_digit(num // 10)
#n = int(input("Введите число: "))
#print(sum_digit(n))
#print(sum(l))

#def sum_digit(n):
#    if n == 0:
#        return 0
#    return n % 10 + sum_digit(n // 10)

#n = int(input("Введите число: "))
#print(sum_digit(n))

#3.	Написать рекурсивную функцию подсчета суммы первых n  членов гармонического ряда:

def sum_harmonic_series(n):
    if n < 2:
        return 1
    return 1 / n + (sum_harmonic_series(n - 1))

print(sum_harmonic_series(int(input("Введите число: "))))
