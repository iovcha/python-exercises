###1
# def summa_n(t):
#     s =0
#     for i in range(1, t + 1):
#         s += i
#     print(f"Я знаю, что сумма чисел от 1 до {t} равна {s}")
#
# summa_n(3)

####2
# def exponentiation(n):
#     print(n ** 2, n ** 3)

###3
# def sum_num(l):
#     s = 0
#     for i in l:
#         if i.isdigit():
#             s += int(i)
#     print(s)

###4
# def get_body_mass_index(weight, growth):
#     growth = growth * 0.01
#     index = weight / growth ** 2
#     if index < 18.5:
#         print('Недостаточная масса тела')
#     elif 18.5 <= index <= 25:
#         print('Норма')
#     else:
#         print('Избыточная масса тела')

###5
# def check_password(psw):
#     upper = [i for i in psw if i.isupper()]
#     digit = [i for i in psw if i.isdigit()]
#     simb = [i for i in "!@#$%*" if i in psw]
#     if len(psw) >= 10 and len(upper) > 0 and len(digit) > 2 and len(simb) >= 1:
#         print('Perfect password')
#     else:
#         print('Easy peasy')

###6
# def count_letters(phraza):
#     n = [i for i in phraza if i.isupper()]
#     k = [i for i in phraza if i.islower()]
#     print(n,k ,sep='\n')
#     # print(f'Количество заглавных символов: {len(n)}')
#     # print(f'Количество строчных символов: {len(k)}')
#
# count_letters('Привет, Старина')

####7
# def repeat_please_n_times(n):
#       for i in range (n):
#           print('Just do it')

###8
# объявление функции
# def is_between(name, surname, middlename):
#     if surname <= name <= middlename or  surname >= name >= middlename :
#         print(True)
#     else:
#         print(False)
#
# # считываем данные
# a, b, c = map(int, input().split())
#
# # вызываем функцию
# is_between(a, b, c)

###9
# объявление функции
# def count_letter(text, letter):
#     count = len([i for i in text  if i == letter])
#     print(count)
#
# # считываем данные
# text = input()
# symbol = input()
# # вызываем функцию
# count_letter(text, symbol)

###10
# объявление функции
# def print_initials(name, surname, middlename):
#     print(f"{surname.title()} {name[0].upper()}.{middlename[0].upper()}.")
#
# # считываем данные
# name = input()
# surname = input()
# middlename = input()
#
# # вызываем функцию
# print_initials(name, surname, middlename)

###11
# assert 200 > 100
# assert [100] * 4 < [100, 100, 100, 10000]
# assert sum([1, 3, 5]) == sum([6, 3])
# assert max(3, -1, 9) == 9
# print('Проверки пройдены')

###12
# def is_person_teenager(age):
#     return 12 <= age <= 17
#
# age = int(input())
# print(is_person_teenager(age))

###13
# def generate_fizz_buzz_list(n):
#     result = []
#     for i in range(1, n + 1):
#         match i:
#             case _  if i % 3 == 0 and i % 5 == 0:
#                 result.append('FizzBuzz')
#             case _ if i % 3 == 0:
#                 result.append('Fizz')
#             case _ if i % 5 == 0:
#                 result.append('Buzz')
#             case _ :
#                 result.append(i)
#     return result
# ###def generate_fizz_buzz_list(n):# еще одно решение
#     #return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or i for i in range(1, n + 1)]
#
# num = int(input())
# result = generate_fizz_buzz_list(num)
# print(result)

###14 NOD нескольких чисел
# from functools import reduce
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a
#
# n = int(input())
# lst = []
# count_elem = 0
#
# for i in range(0, n):
#     elem = int(input())
#     lst.append(elem)
#     while count_elem < len(lst):
#         gcd_rezult = reduce(gcd, lst)
#         count_elem += 1
# print(gcd_rezult)
##### решение без модулей НОД для нескольких чисел
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a
#
# n=int(input())
# a=int(input())
# for i in range(n-1):
#     b=int(input())
#     a=gcd(a, b)
# print(a)

###15
# def find_duplicate(lst):
#     a = []
#     for i in lst:
#         if i not in a and lst.count(i) > 1:
#             a.append(i)
#     return a
#
#
# assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
# assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
# assert find_duplicate([1, 2, 3, 4]) == []
# assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
# print('Все успешно')


####16
# def first_unique_char(s):
#     for i in range(len(s)):
#         if s.count(s[i]) == 1:
#             return s.index(s[i])
#     return -1
#
#
# s = input()
# print(first_unique_char(s))

####17
# def format_name_list(names: list):
#     a = []
#     for i in names:
#         a.append(i['name'])
#     if len(a) == 0:
#         return ""
#     elif len(a) == 1:
#         return a[0]
#     else:
#         if len(a) == 2:
#             return f'{a[0]} и {a[1]}'
#         else:
#             b = ''
#             for i in range(1, len(a) - 1):
#                 b += (a[i - 1] + ', ')
#             b += f'{a[-2]} и {a[-1]}'
#             return b
# ####return ', '.join(names[:-1]) + ' и ' + names[-1]

#####18
# def get_domain_name(url):
#     if '//' in url:
#         a = url.split('//')
#         if 'www' in a[1]:
#             a[1] = a[1].split('.')
#             return a[1][1]
#         else:
#             a[1] = a[1].split('.')
#             return a[1][0]
#     else:
#         if 'www' in url:
#             a = url.split('.')
#             return a[1]
#         else:
#             a = url.split('.')
#             return a[0]
####url = url.replace("http://", "").replace("https://", "").replace("www.", "")
##print(url.split('.')[0])

###19
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n):
    a = []
    for i in range(len(str(factorial(n))) - 1, -1, -1):
        if str(factorial(n))[i] == '0':
            a.append(0)
        else:
            if str(factorial(n))[i - 1] != '0':
                break
    return len(a)

###20
def count_AGTC(dna):
    a = [dna.count('A'), dna.count('G'), dna.count('T'), dna.count('C')]
    return tuple(a)

####через словарь
# def count_AGTC(dna: str):
#     d = dict.fromkeys('AGTC', 0)
#     for c in dna:
#         d[c] += 1
#     return tuple(d.values())
# print(count_AGTC('AGGTC'))