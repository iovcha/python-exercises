#1.	Выведите на экран все числа в интервале от 1500 до 2700 включительно, которые кратны 7
# и имеют среди своих множителей число 5.
i = 1500
while i <= 2700:
    i += 1
    if i % 7 == 0 and i % 5 == 0:
        print(i)

#2.	Выведите на экран все числа в интервале от 0 до 6 включительно, кроме чисел 3 и 5.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    elif i == 5:
        continue
    print(i)

#3.	Выведите на экран все числа в интервале от 100 до 400 включительно, каждое из которых состоит только из четных
#цифр. Например: 200, 260, 282, 400 и
i =100
while i <= 400:
    i += 1
    if (i % 10) % 2 == 0 and ((i // 10) % 10) % 2 == 0 and (i // 100) % 2 == 0:
        print(i)

#4.	Напишите программу для расчета факториала числа N, т.е. произведения всех чисел от 1 до N включительно
n = int(input())
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)

#5.	Найдите сумму чисел в следующей последовательности: 2, 22, 222, 2222, …, 2(n),
# - где n - количество разрядов в последнем числе.
# Например, при n = 5 последнее число будет 22222, а сумма чисел в последовательности 24690.
a = '2'
n = 5
s = '0'
i = 0
while n > 0:
    i = int(a * n)
    n = n - 1
    s = int(s) + i
    print(i, s)

#вывод чисел по убыванию порядке
i = int(input("Введите число : "))
while i > 1:
    i -= 1
    print(i, end=' ')


#вывод чисел по возрастанию
i = int(input("Введите число : "))
n = 0
while n < i:
    n += 1
    print(n, end=' ')










