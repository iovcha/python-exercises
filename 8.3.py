#1.	Определить, сколько раз последовательность из N произвольных чисел меняет знак
# (т.е. после положительного элемента идет отрицательный и наоборо
#line = input("Введите число: ")
#s = []
#count = 0
#while line != "":
#    num = int(line)
#    s.append(num)
#    line = input("Введите число: ")
#    count = 0
#    for i in range(0, len(s) - 1):
#        if (s[i] >= 0 and s[i + 1] < 0 ) or (s[i] < 0 and s[i + 1] >= 0):
 #           count += 1
#print(f"Последовательность  меняла знак {count} раз")
#print(s)

#2.	Дан некоторый текст. Определить количество вхождений в него каждого символа.
#text ="	Дан некоторый текст."
#dict = {symbol: text.count(symbol) for symbol in text}
#print(dict)
#text ="Дан некоторый текст."
#dict = {}
#for symbol in text:
    #if symbol in dict.keys():
        #dict[symbol] += 1
    #else:
        #dict[symbol] = 1
#print(dict)


#33.	Вывести на экран следующую последовательность символов:
#	* * * * * * *
#	  * * * * *
#	    * * *
#	      *
#	    * * *
#	  * * * * *
#	* * * * * * *

#symbols = '*'
#n = 7
#for i in range(n, 0, -2):
#    s = str(symbols * i)
#    t = int((n - len(s)) / 2)   #количество знаков,которые необходимо добавить с одной стороны
#    s = s.rjust(t + len(s))#общее клоичество символов в строке
 #   print(s)


#for i in range(3, n + 1, 2):
#    s = str(symbols * i)
#    t = int((n - len(s)) / 2)  # количество знаков,которые необходимо добавить с одной стороны
#    s = s.rjust(t + len(s))
#    print(s)

#4.	Найти среднее арифметическое делителей числа N.
N = int(input("Введите число: "))
num_list = []
for i in range(1, N +1):
    if N % i == 0:
        num_list.append(i)
        arith_mean = sum(num_list) / len(num_list)
print(num_list, round(arith_mean, 2))

















