#Таблица 2.8. Канадские праздники
#Праздник Дата
#Новый год 1 января
#День Канады 1 июля
#Рождество 25 декабря
#Напишите программу, которая будет запрашивать у пользователя день
#и  месяц. Если введенные данные в точности указывают на один из перечисленных в таблице праздников, необходимо вывести его название
#В противном случае сообщить, что на заданную дату праздники не приходятся.
#new_year = '1 января '
#day_canada = ' 1 июля'
#christmas = '25 декабря'
day = int(input('Введите день : '))
month = str(input('Введите  месяц: '))
celebration = ''
if day == 1 and month == 'January':
    celebration = 'New year'
elif day == 1 and month == 'July':
    celebration =' Day Canada'
elif day == 25 and month == 'December':
    celebration = 'Christmas'
if celebration == '':
    print('на заданную дату праздники не приходятся.')
else:
    print('Это - ', celebration)