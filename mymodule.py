
def count_rank_number(n):#розряд числа
    count = 1
    n //= 10
    while n > 0:
        n //= 10
        count += 1
    return count

username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
password_correct = False
count = 0

while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
        count += 1
    elif username in password:
        print('Пароль содержит имя пользователя\n')
        count += 1
    else:
        print('Пароль для пользователя {} установлен'.format(username))
        password_correct = True
        continue
    password = input('Введите пароль еще раз: ')
    if count == 3:
        print('Использовано 3 попытки ,попробуйте позже')
        break

#9. Наибольший общий делитель

#n = int(input("Введите целое положительное : "))
#m = int(input("Введите целое положительное число: "))
#if n < m:
#    r = n % m
#    while r != 0:
#        n = m
#        m = r
#        r = n % m
#    print(m)
#else:
#    print("Не корректный ввод, первое число должно быть меньше второго")

#0. Простые множители

#n = int(input("Введите число: "))
#l = list()
#factor = 2
#while n < factor:
#    print('error')
#    break
#while factor <= n:
#    if n % factor == 0:
#        l.append(factor)
#        n = n / factor
#    else:
#        factor += 1
#print(l)

#Десятичное число в двоичное
#rezult = []
#g = int(input('Введите целое число:'))

#while True:
#    r = g % 2
#    r = str(r)
#    rezult.insert(0, r)
#    g = g // 2
#    if g == 0:
#        break
#rezult =[int(r) for r in rezult]
#rezult = "".join(map(str, rezult))
#print("двоичное число", rezult )

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


#Напишите программу, которая проверяет, является ли введённое натуральное число степенью двойки.
x = int(input())
i = 0
while x % 2 == 0 :
    x = x // 2
    i += 1
if x == 1 :
    print(i)
else:
    print("НЕТ")
#делители
n = int(input())
i = 1
a = []
while i ** 2 <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)

N, k = list(map(int, input().split()))
kegelban = ['I'] * N
for i in range(k):
    start, end = list(map(int, input().split()))
    for j in range(start - 1, end):
        kegelban[j] = '.'
print(''.join(kegelban))

def create_file_with_numbers(n):
    """Функция должна создать файл с название "range_<number>.txt" и
     наполнить его целыми числами от 1 до n включительно,
     причем каждое число записывается  в отдельной строке"""
    with open(f'range_{n}.txt', mode='w', encoding='utf-8') as fw:
        fw.write('\n'.join(map(str, range(1, n + 1))))


#Для поиска самого длинного слова:

with open('test.txt', 'r', encoding='utf-8') as f:
  longest_word = max(f.read().split(), key=lambda i: len(i))
#Для добавления найденного слова в конец файла в верхнем регистре:

with open('test.txt', 'a', encoding='utf-8') as f:
  f.write('\n' + longest_word.upper())