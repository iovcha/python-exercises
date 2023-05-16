# 1.	Написать рекурсивную функцию подсчета суммы элементов списка чисел.

# def sum_arr(arr, size):#size длинна списка
#    if (size == 0):
#        return 0
#    else:
#        return arr[size - 1] + sum_arr(arr, size - 1)
# n = int(input("Введите длину списка:"))
# a = []
# for i in range(0, n):
#    element = int(input("Введите элемент списка:"))
#    a.append(element)
# print("Весь список:")
# print(a)
# print("Сумма элементов списка равна:")
# b = sum_arr(a, n)
# print(b)

# 2.	Написать рекурсивную функцию подсчета суммы цифр положительного целого числа.

# l = []
# def sum_digit(num):
#    if num == 0:
#        return l
#    dig = num % 10
#    l.append(dig)
#    sum_digit(num // 10)
# n = int(input("Введите число: "))
# print(sum_digit(n))
# print(sum(l))

# def sum_digit(n):
#    if n == 0:
#        return 0
#    return n % 10 + sum_digit(n // 10)

# n = int(input("Введите число: "))
# print(sum_digit(n))

# 3.	Написать рекурсивную функцию подсчета суммы первых n  членов гармонического ряда:

# def sum_harmonic_series(n):
#     if n < 2:
#         return 1
#     return 1 / n + (sum_harmonic_series(n - 1))
#
# print(sum_harmonic_series(int(input("Введите число: "))))

###4
def print_from(n: int) -> None:
    print(n)
    if n > 1:
        print_from(n - 1)


###5
def print_to(n: int) -> None:
    """распечатывает на экране последовательность целых чисел от 1 до n включительно. """
    if n > 0:
        print_to(n - 1)
        print(n)


###6
def string_reverce(n: int):
    """Требуется вывести  последовательность в обратном порядке."""
    if n > 0:
        string_reverce(n - 1)
        print(s[-n], end=' ')


#
# n = int(input())
# s = list(map(int, input().split()))
#
# string_reverce(n)

###7
def double_fact(n: int):
    """Двойной факториал"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return double_fact(n - 2) * n


###8
def tribonacci(n: int):
    """Числа Трибоначчи"""
    if n == 0 or n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


###9
def get_combin(n: int, k: int):  # n > 0, 0 ≤ k ≤ n
    """число сочетаний """
    if k == 0 or k == n:
        return 1
    return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


###10
def ackermann(m: int, n: int) -> int:
    """Функция Аккермана"""
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


###11
def list_sum_recursive(l: list) -> int:  # n == len(l)
    """принимает на вход список из целых чисел и возвращает сумму элементов"""
    if len(l) == 1:
        return l[0]
    return l[0] + list_sum_recursive(l[1:])


def flatten(l: list) -> list:
    """Превращаем вложенный список в плоский"""
    if not l:
        return []
    if isinstance(l[0], list):
        return flatten(l[0]) + flatten(l[1:])
    return l[:1] + flatten(l[1:])


####13

def flatten_dict(nested: dict, key: str = '') -> dict:
    """Превращаем вложенный словарь в плоский"""
    d = {}
    for key, value in nested.items():
        if isinstance(value, int):
            d.update({key: value})
        if isinstance(value, dict):
            for k, v in flatten_dict(value).items():
                d.update({key + "_" + k: v})
    return d


# assert flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}) == {'Q_w_E_r_T_y': 123}

####14
def merge_two_list(a, b):
    """функция merge_two_list должна объединить два списка"""
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    if i < len(a):
        res += a[i:]

    if j < len(b):
        res += b[j:]
    return res


def merge_sort(s):
    """функция merge_sort должна выполнить сортировку"""
    if len(s) == 1:
        return s
    middle = len(s) // 2
    middle_left = merge_sort(s[:middle])
    middle_right = merge_sort(s[middle:])
    return merge_two_list(middle_left, middle_right)


# n = int(input())
# s = list(map(int, input(). split()))
# print(*merge_sort(s))
####15

# print(s[int((len(s) / 2))] if len(s) % 2 else s[int((len(s) / 2 - 1)):int((len(s) / 2)) + 1]) нахождение среднего элемента
def quick_sort(s: list):
    """Быстрая сортировка """
    if len(s) <= 1:
        return s
    elem = s[int(len(s) // 2)]  # можно взять любой элемент , например s[0] or s[-1] or s[1] он от которого отталкиваються
    left = [i for i in s if i < elem]
    centr = [i for i in s if i == elem]
    right = [i for i in s if i > elem]
    return quick_sort(left) + centr + quick_sort(right)


###16
import os


def obchodFile(path: str, level=1):  # path путь папки в проводнике
    """Рекурсивный обход файлов"""
    print("Level=", level, "Content:", os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print("Спускаемся", path + '\\' + i)
            obchodFile(path + '\\' + i, level + 1)
            print("Возвращаемся", path)


###17
def reverce_num(n: int):
    """Цифры числа справа налево"""
    if n < 10:
        return n
    else:
        print(str(n % 10), end=' ')
    return reverce_num(n // 10)


# print(reverce_num(678781))

###18
def rec_num(n: int):
    """Цифры числа слева направо"""
    if len(str(n)) == 1:
        return str(n)[0]
    return (str(n)[0]) + ' ' + rec_num(int(str(n)[1:]))


def recur_num(n: int):
    """Цифры числа слева направо"""
    if n < 10:
        return n
    return str(recur_num(n // 10)) + ' ' + str(n % 10)


# print(recur_num(3675))

###19
def simple_num(n: int, i=None):
    """Проверка числа на простоту"""
    if i is None:
        i = n - 1
    while i >= 2:
        if n % i == 0:
            print("No")
            return False
        else:
            return simple_num(n, i - 1)
    else:
        print('Yes')
        return True


###20
def divide(n, d=2):
    """Разложение на множители"""
    flag = False
    while d ** 2 <= n:
        if n % d == 0:
            print(d, end=" ")
            divide(n // d)
            flag = True
        d += 1
    if not flag:
        print(n)


####21
def polindrom(s: str):
    """Палиндром"""
    if len(s) <= 1:
        print('Yes')
        return True
    if s[0] != s[-1]:
        print('No')
        return False
    return polindrom(s[1:-1])


###22
def odd_num(n:str):
    """Вывести нечетные числа последовательности"""
    if len(n) == 1:
        return n[0]

    if int(n[0]) % 2 == 1:
        print(int(n[0]), end=' ')
    return odd_num(n[1:])


