#. . Таблица умножения

# Строка заголовков
#print(" ", end="")
#for i in range(1, 11):
#    print("%4d" % i, end="")
#print()
# Выводим таблицу
#for i in range(1, 11):
#    print("%4d" % i, end="")
#    for j in range(1, 10):
#        print("%4d" % (i * j), end="")
 #   print()


#. Гипотеза Коллатца

#while True:
#    number = int(input("Введите стартовое число (ноль или отрицательное для выхода): "))
#    if number <= 0:
#        break
#    while number != 1:
#        if number % 2 == 0:
#            number = number // 2
#        else:
#            number = 3 * number + 1
#        print(number, end=' ')
#        print()

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

#Двоичное число в десятичное
#num = str(input("Введите двоичное число: "))
num_des = 0
#for i in range( 0, len(num)):
 #   num_des = num_des + int(num[i]) * (2 ** (len(num) - 1 - i))
 #   print(num_des)

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


#3. Максимальное числов последовательности
#from random import randrange
#max_value = randrange(1, 101)
#print(max_value)
#count_max = 0
#for i in range(1, 101):
#    # Генерируем новое случайное число
 #   current = randrange(1, 101)
 #   if current > max_value:
#        max_value = current
 #       count_max += 1
 #       print(current,"<== Обновление")
#    else:
 #       print(current)

#print("Максимальное значение в ряду:", max_value)
#print("Количество смен максимального значения:", count_max  )


#. Подбрасываем монетку
import random
total_attempts = 0
for i in range(10):
    result = []
    current = ''
    nexxt = ''
    count = 1
    attempts = 0
    while True:
        nexxt = random.choice('ОР')
        result.append(nexxt)
        attempts += 1
        if nexxt == current:
            count += 1
            if count == 3:
                break
        else:
            count = 1
        current = nexxt
    total_attempts += attempts
    print(''.join(result), f'(попыток: {attempts})')
print('Среднее количество попыток:', total_attempts / 10)







