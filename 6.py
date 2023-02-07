#. Среднее значение
#n = int(input("Введите количество элементов списка: "))
#a = []
#for i in range(0, n):
 #   elem = int(input("Введите элемент списка: "))
#    a.append(elem)
#    if a[0] == 0:
#        print('error')
#        exit(0)
#if elem == 0:
#    avg = sum(a) / (n - 1)
#else:
#    avg = sum(a) / n
#print("Среднее значение элементов списка", round(avg, 2))

#Таблица со скидками
#purchase_sum = [4.95, 9.95, 14.95, 19.95, 24.95]#сумма покупки
#for i in purchase_sum:
 #   discount = i * 0.6
 #   new_price = i - discount
  #  print(" Сумма покупки =% .2f" % i,  "Скидка составляет %.2f." % discount, "Новая цена =%.2f" % new_price )

#. Таблица соотношения температур
#for t_celsus in range(0, 101):
 #   if t_celsus % 10 == 0:
 #       t_pharyngate = t_celsus * 1.8 + 32
  #      print(t_celsus, "градусам целсия соответствует", t_pharyngate, "по фаренгейту")

#Никаких центов
total = 0.00
price = input("Введите цену товара (пустая строка для выхода): ")
while price != '':
    total = float(price) + total
    price = input("Введите цену товара (пустая строка для выхода): ")
print("Полная сумма к оплате:  %.2f." % total)
a = total * 100 % 5
print(a)




