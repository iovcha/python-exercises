# Вычисляем длину гипотенузы
#a = float(input("Введите длинну  катетa: "))
#b = float(input("Введите длинну  катетa: "))

#from math import sqrt

#def hypotenuse(a, b):
#    return sqrt(a ** 2 + b ** 2)

#print(round(hypotenuse(a, b), 2))

#. Плата за такси

#baz_tarif = 4.00
#dop_tar = 0.25
#l = 0.14 # km

#distance = float(input("Сколько километров вам нужно проехать? "))

#def total_sum(n):
#    count = distance // l
#    dop_tar_dist = count * dop_tar
#    tarif = baz_tarif + dop_tar_dist
#    return tarif

#print(total_sum(distance))

#. Расчет стоимости доставки

#cena_1goods = 10.95
#each_good = 2.95

#count_goods = int(input("количество товаров в  заказе: "))

#def delivery_amount(n):
#    summa = round(cena_1goods + (count_goods - 1) * 2.95, 2)
#    return summa

#print(delivery_amount(cena_1goods))

#Напишите функцию, которая будет принимать на вход три числа в качестве параметров
# и возвращать их медиану. В основной программе должен
#производиться запрос к пользователю на предмет ввода трех чисел, а также вызов функции и отображение результата.
#a = float(input("Введите число: "))
#b = float(input("Введите число: "))
#c = float(input("Введите число: "))
#list_num = []
#list_num.append(a)
#list_num.append(b)
#list_num.append(c)
#list_num_sort = sorted(list_num)
#print(list_num_sort)

#import statistics
#print(statistics.median(list_num_sort))#как вариант через statistics

#a = int(input("Введите число: "))
#b = int(input("Введите число: "))
#c = int(input("Введите число: "))

#def median(a, b, c):
 #   if (a > b and b > c) or (a > b and b < c) :
 #       return b
#    if (b < a and a < c) or (b > a and a > c):
#        return a
#    if (c < a and b < c ) or (c > a and b > c ):
#        return c
#print("Медиана равна:", median(a, b, c))

#. Переводим целые числа в числительные
num = int(input("Введите число: "))

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
print(numeral(num))