#Тема 5: “Условие else в циклах”
#1.	Дана последовательность чисел. Проверить, есть ли в ней хотя бы одно число
# с делителями 2, 5 и 7. Если да, вывести его на экран. Если нет, вывести соответствующее сообщение.
#from random import randint
#num = int(input("Задайте размерность массива : "))

#arr = []
#list_num = []
#for _ in range(num):
#    arr.append(randint(4, 16))

#    for i in arr:
 #       if i % 2 == 0 and i % 5 == 0 and i % 7 == 0:
 #           list_num.append(i)
#            print("Числа с делителями 2, 5 и 7 :", list_num)
#            break
#else:
#    print("Таких чисел нет")
#print(arr)

#2.	Дана последовательность чисел. Проверить, являются ли все элементы последовательности нечетными числами.
#from random import randint
#num = int(input("Задайте размерность массива : "))

#arr = []
#for _ in range(num):
#    arr.append(randint(4, 16))

#for i in arr:
 #   if i % 2 == 0:
#        print("все элементы последовательности не являются  нечетными числами")
#        break
#else:
#    print("все элементы последовательности нечетными числами.")

#3.	Дан список продуктов с ценами на них: ‘milk’ - $12, ‘bread’ - $10, ‘meat’ - $60, ‘vegetable mix’ - $20,
# ‘fruit mix’ - $35, ‘fish’ - $45, ‘eggs’ - $15, ‘cake’ - $15. У Марты есть $100.
# Какое максимальное количество продуктов она может купить?
# Выведите на экран список этих продуктов. В случае если Марта сможет купить все продукты
#из списка, выведите соответствующее сообщение. Решите эту же задачу для Алекса, у которого есть $250.

list_prod = {"milk": 12, "bread": 10, "meat": 60, "vegetable mix": 20, "fruit mix": 35, "fish": 45, "eggs": 15, "cake": 15}
list_prod2 ={"bread": 10, "milk": 12, "eggs": 15, "cake": 15,"vegetable mix": 20, "fruit mix": 35, "fish": 45,"meat": 60}


count = 0
summa_prod = int(input("Сколько у вас денег ? "))
for prod, price in list_prod2.items():
    summa_prod -= price
    if summa_prod < 0:
        print("Максимальное коллисество продуктов : ", count)
        break
    count += 1
    print(prod, end=' ')
else:
    print("Марта сможет купить все продукты")










