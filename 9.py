#1.	Дана последовательность целых чисел. Для каждого числа последовательности найти количество его делителей.
from random import randint
num = int(input("Задайте размерность массива : "))

arr = []
for _ in range(num):# Выражение for _ in range(num) обычно используется просто для того, чтобы повторить что-то num раз
    arr. append(randint(2, 25))
print(arr)
def count_divisor(n):
    for n in arr:
        i = 1
        a = []
        while i ** 2 <= n:#нахождение делителей
            if n % i == 0:
                a.append(i)
                if i != n // i:
                    a.append(n // i)
            i += 1
        a.sort()
        print("Количество делителей последовательности для  числа ", n, " = ", len(a))
count_divisor(arr)