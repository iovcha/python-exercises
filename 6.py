#pasword = input('Введите пароль: ')
#cond1 = any( [True if len(pasword) >= 5 else False])
#print(cond1)
#cond2 = any([True if not pasword.islower() and not pasword.isupper() else False])
#print(cond2)
#cond3 = any([True if set(pasword).intersection({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}) else False])
#print(cond3)
#cond4 = any([True if set(pasword).intersection({'%','#','&','@'}) else False ])
#print(cond4)
#print('ПАроль надёжный ?', cond1 and cond2 and cond3 and cond4)
#print('ПАроль надёжный ?',cond1 and cond2 and cond3)

#3.	Напишите программу расчета “человеческого” возраста для собаки.
# Расчет должен производиться следующим образом: первые два года жизни каждый год эквивалентен 10.5 человеческим годам,
# далее каждый год может быть приравнен к 4 человеческим годам.

#age_dog = float(input('Вoзраст вашей собаки: '))
#if age_dog <= 2:
  #  print('Возраст собаки = ', age_dog * 10.5,'человеческих лет')
#else:
    #print('Возраст собаки = ', (age_dog - 2) * 4 + 21)

#4.	В магазине продаются следующие товары: smart watch ($600), phone ($1000), playstation ($450), laptop ($1550),
# music player ($400) и tablet ($400). Майкл хочет сделать подарок родителям.
# В магазине проводится акция: если он купит товары на $1000, то любой следующий товар он получит со скидкой 30%.
# У Майкла есть $1300. Хватит ли у него денег,
# чтобы купить музыкальный плеер маме, умные часы папе и плейстейшн себе?

goods = {'smart watch': 600, 'phone': 1000, 'playstation': 450, 'laptop': 1550, 'musik player': 400, 'tablet': 400}
dolars = 1300
buy = any([True if goods['musik player'] + goods['smart watch'] == 1000 else False])
if buy == 1:
    print('discount 30% ', goods['playstation'] * 0.3 )
    print('Стоимость товара со скидкой ', goods['playstation'] - (goods['playstation'] * 0.3))
else:
      print('скидки нет')
buying_yourself = any([True if dolars - (goods['musik player'] + goods['smart watch']) >
                              (goods['playstation'] - (goods['playstation'] * 0.3)) else False])
print('Денег хватает ', buying_yourself)

#from math import sqrt
#a = float(input('Введите число: '))
#b = float(input('Введите   число: '))
#c = float(input('Введите число: '))
#d = b**2 - 4*a*c
#print('d = ', d)
#if d >= 0:
#    y1 = (-b + sqrt(d)) / (2 * a)
#    y2 = (-b - sqrt(d)) / (2 * a)
 #   print('y1 = %.2f.' % y1, 'y2 = %.2f.' % y2)
 #   if y1 >= 0 and y2 >= 0:
 #       x1 = sqrt(y1)
 #       x2 = -x1
#        x3 = sqrt(y2)
#        x4 = -x3
 #       print('x1 = %.2f.' % x1, 'x2 = %.2f.' % x2, 'x3= % .2f.' % x3, 'x4= %.2f.' % x4)
#
#else:
   # print('Корней нет')











