#1
#summa = 0
#count = 0
#for i in range(1, 9):
 #   summa += i
#    count += 1
#    if summa == 15:
#        break
#print(summa, count)

#summa = 0
#count = 0
#i = 1
#while i < 9:
#    summa += i
#    count += 1
#    i += 1
#    if summa == 15:
#        break
#print(summa, count)

#2
#for n in range(5, 25):
#    if n % 3 == 0 or n % 6 == 0:
#        continue
#    elif n % 5 == 0:
#        print(n, "кратно 5")
#        continue
#    print(n)

#3
#list = ['Rose', 'Nina', 'Phillip', 'Alex', 'Jimmy', 'Max']

#for name in list:
   # if len(name) < 5:
   #     if 'x' in name:
    #        print("Hello,", name)
    #        break
    #    else:
     #       print("Hello,", name)

#4
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

password_correct = False

while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
    else:
        print('Пароль для пользователя {} установлен'.format(username))
        password_correct = True
        continue
    password = input('Введите пароль еще раз: ')









