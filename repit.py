# Напишите функцию, которая принимает положительный параметр num и
# возвращает его мультипликативную продолжительность, которая представляет собой
# количество раз, когда вы должны умножать цифры в num,
# пока не достигнете одной цифры. Пример: Persistence(39) == 3 // так как 3*9 = 27, 2*7 = 14, 1*4=4


def multipler(n):
    pr = 1
    while n > 0:
        digit = n % 10
        pr *= digit
        n = n // 10
    if len(str(pr)) == 1:
        return pr
    return multipler(pr)


#


def char_concat(s, level=1):
    """Учитывая строку, вам необходимо постепенно объединить первую букву слева
     и первую букву справа и «1», затем вторую букву слева и вторую букву справа и «2» и так далее."""
    if len(s) % 2 == 1:
        s.replace(s[len(s) // 2], '')

    return s[0] + s[-1] + str(level) + char_concat(s[1:-1], level + 1) if len(s) > 1 else ''


# print(char_concat("$'D8KB)%PO@s"))


def char_concat1(s):
    return ''.join([s[i] + s[len(s) - 1 - i] + str(i + 1) for i in range(len(s) // 2)])


def sum_of_integers_in_string(s):
    """Сумма целых чисел в строке"""
    l = []
    n = ''

    for i in s:
        if i.isdigit():
            n += i
        else:
            if n.isdigit():
                l.append(int(n))
                n = ''
    if n != '':
        l.append(int(n))
    return sum(l)


# s = "1bcdefghijklmnopqrstuvwxyz"
# letters = [0] * 26
# for i in s.lower():
#     if i >= "a" and i <= "z":
#         nomer = ord(i) - 97
#         letters[nomer] += 1
# print(letters)
# print(all(x != 0 for x in letters))

def longest_consec(strarr, k):
    '''Вам дан массив (список) strarrстрок и целое число k.
    Ваша задача — вернуть первую самую длинную строку, состоящую из k последовательных строк, взятых в массиве.'''
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''

    longest = index = 0
    for i in range(n - k + 1):
        length = sum([len(s) for s in strarr[i: i + k]])
        if length > longest:
            longest = length
            index = i

    return ''.join(strarr[index: index + k])


def unique_in_order(sequence):
    res = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i - 1]:
            res.append(sequence[i])
    return res


# print(unique_in_order('ABBCcA'))

def sort_array(lst):
    '''Вам будет предоставлен массив чисел.
    Вам нужно отсортировать нечетные числа в порядке возрастания, оставив четные числа на исходных позициях.'''
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            for j in range(len(lst)):
                if i != j and lst[j] % 2 != 0:
                    if lst[i] < lst[j]:
                        lst[i], lst[j] = lst[j], lst[i]
    return lst


# fib1 = 1
# fib2 = 1
#
# n = int(input())
#
# print(fib1, fib2, end=' ')
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')


def tribonacci(signature, n: int):
    """Числа Трибоначчи"""

    f1 = signature[0]
    f2 = signature[1]
    f3 = signature[2]

    # f1, f2, f3 = 1, 1, 1
    l = []
    for _ in range(n):
        l.append(f1)
        f1, f2, f3 = f2, f3, f1 + f2 + f3
    return l


def delete_nth(order, max_e):
    """Удалить вхождения элемента, если он встречается более n раз"""
    temp = {}
    res = []
    for i in order:
        if i not in temp:
            temp[i] = 0
        else:
            temp[i] += 1
        if temp[i] < max_e:
            res.append(i)
    return res


def delete_nth1(order, max_e):
    """Удалить вхождения элемента, если он встречается более n раз"""
    d = {}
    new_order = []
    for i in order:
        d[i] = d.get(i, 0) + 1
        if d[i] <= max_e:
            new_order.append(i)
    return new_order


# print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))

def queue_time(customers, n):
    '''Очередь в супермаркете. написать функцию для расчета общего времени,
     необходимого всем клиентам для оформления заказа!'''
    if len(customers) == 0:
        return 0
    elif sum(customers) < n:
        return max(customers)
    else:
        time = [0] * n
        for i in customers:
            time.sort()
            time[0] += i
        return max(time)


# print(queue_time([10, 2, 3, 3], 3))

def get_sum(a, b):
    # good luck!
    if a == b:
        return a
    s = 0
    for i in range(min(a, b), max(a, b) + 1):
        s += i
    return s


# print(get_sum(0, -1))

def max_sequence(arr):
    """Максимальная сумма подмассива. Алгоритм Кадане
    """
    if len(arr) == 0:
        return 0
    max_till_now = arr[0]
    max_ending = 0
    for i in range(len(arr)):
        max_ending += arr[i]
        if max_ending < 0:
            max_ending = 0
        elif max_till_now < max_ending:
            max_till_now = max_ending
        return max_till_now


# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# s = 'take me to semynak'
# arr, num_list = s.lower().split(), []
# for i in arr:
#     num = 0
#     letters = list(i)
#     for word in letters:
#         num += ord(word) - 96
#     num_list.append(num)
# print(arr[num_list.index(max(num_list))])

def wave(people):
    """создать функцию, которая превращает строку в мексиканскую волну."""
    if len(people)== 0:
        return []
    else:
        people = people.lower()
        the_wave = []
        for i,j in enumerate(people):
            if j == ' ':
                continue
            else:
                the_wave.append(people[:i] + people[i].upper() +people[(i + 1):])
        return the_wave













