def numeral(num):
    match num:
        case 1: return "First"
        case 2: return "Second"
        case 3: return "Thid"
        case 4: return "Fouth"
        case 5: return "Fifth"
        case 6: return "Sixth"
        case 7: return "Seventh"
        case 8: return "Eighth"
        case 9: return "Ninths"
        case 10: return "Tenth"
        case 11: return "Eleventh"
        case 12: return "Twelfth"
        case _: return ""

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