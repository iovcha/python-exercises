#1
#list_num = [5,  23, 9]

#count = 0
#for n in list_num:
#    if n % 2 == 0:
 #       print('Четное число присутствует')
 #       count += 1
 #   if count == 1:
 #       print('Четное число: ', n)
 #       break
#else:
#    print("четных чисел нет")

#2
#s = "Python else loop"

#for i in range(0, len(s)):
#    if s[i] == 'l':
#        print('Yes')

 #       if 'a' == s[i+1] or 'o' == s[i+1] or 'e' == s[i+1]:
#           print('Есть комбо', s[i] + s[i+1])
#           break
#        else:
#            print('Комбо не найдены')
 #           break
#else:
 #    print('l нет')

#3
#Перепишите программу проверки надежности пароля из предыдущего урока, ограничив количество попыток ввода пароля.
#Если за три попытки пароль так и не был установлен, вывести соответствующее сообщение на экран.

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
    if count > 2:
        print('Использовано 3 попытки ,попребуйте позже')
        break






