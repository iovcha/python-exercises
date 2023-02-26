#1.	Дана последовательность целых чисел. Для каждого числа последовательности найти количество его делителей.
#from random import randint
#num = int(input("Задайте размерность массива : "))

#arr = []
#for _ in range(num):# Выражение for _ in range(num) обычно используется просто для того, чтобы повторить что-то num раз
#    arr. append(randint(2, 25))
#print(arr)
#def count_divisor(arr):
#    for n in arr:
#        i = 1
#        a = []
#        while i ** 2 <= n:#нахождение делителей
 #           if n % i == 0:
#                a.append(i)
#                if i != n // i:
#                    a.append(n // i)
#            i += 1
#        a.sort()
#        print("Количество делителей последовательности для  числа ", n, " = ", len(a))
#count_divisor(arr)

#2.	Дана последовательность целых чисел. Найти в каждом числе сумму четных цифр.
#from random import randint
#num = int(input("Задайте размерность массива : "))

#arr = []
#for _ in range(num):# Выражение for _ in range(num) обычно используется просто для того, чтобы повторить что-то num раз
#    arr. append(randint(2, 2000))
#print(arr)

#def sum_even_numbers(arr):
#    m = []
 #   for i in arr:
#        summa = sum(int(a) for a in str(i) if a in '2468')
#        m.append(summa)
#    print(m)
#sum_even_numbers(arr)

#3.	Дана последовательность целых чисел. Для каждого числа последовательности проверить,
# представляют ли его цифры строго возрастающую последовательность.

#from random import randint
#num = int(input("Задайте размерность массива : "))

#arr = []
#for _ in range(num):# Выражение for _ in range(num) обычно используется просто для того, чтобы повторить что-то num раз
#    arr. append(randint(20, 2000))
#print(arr)

#def ascending_sequence(arr):
 #   b = []
#    c = []
 #   for x in arr:
 #       k = [int(a) for a in str(x)]
 #       b.append(k)
 #   for t in b:
#        a = all(t[i - 1] < t[i] for i in range(1, len(t)))#Функция all() всегда возвращает False или True
#        c.append(a)
 #   print(c)
#ascending_sequence(arr)


#4.	Дан диапазон целых чисел от n1 до n2. Найти факториал каждого третьего простого числа в заданном диапазоне.
#n1 = int(input("Введите начало диапазона для поиска простых чисел: "))
#n2 = int(input("Введите конец диапазона для поиска простых чисел: "))
#l = list(range(n1, n2 +1))
#print(l)
#def is_prime(n):
#    for i in range(2, (n // 2) + 1):
#        if n % i == 0:
 #           return False
#    return True

#def is_neutral(n):
#    return n in [0, 1]

#def factor(n):
 #   f = 1
#    for i in range(1, (n + 1)):
#        f *= i
#    return f

#prime_num = []
#factor_list = []
#for i in l:
 #   if is_neutral(i):
#        continue
 #   if is_prime(i):
 #       prime_num. append(i)


#for i in prime_num:
#    for j in range(0, len(prime_num), 2):
#        if prime_num[j] == 2:
#            continue
 #       if prime_num[j] == i:
#            fact = factor(i)
#            factor_list.append(fact)

#print(prime_num)
#print(factor_list)

#5.	Дано натуральное число N.
# Уменьшить число в 2 раза (деление нацело) и проверить, изменилось ли после уменьшения количество разрядов в числе.
N = int(input("Введите натуральное число: "))

def count_rank_number(n):
    count = 1
    n //= 10
    while n > 0:
        n //= 10
        count += 1
    return count

n = N // 2
if count_rank_number(N):
    pass#print(count_rank_number(N))
if count_rank_number(n):
    pass#print(count_rank_number(n))
if count_rank_number(N) == count_rank_number(n):
    print("количество разрядов в числе не изменилось")
else:
    print("количество разрядов в числе  изменилось")




