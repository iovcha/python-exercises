# метод Ньютона.. Квадратный корень
from math import e
x = float(input('Задайте число: '))
guess = x / 2
while guess * guess - x > 10e-12:
    guess = (guess + (x / guess)) / 2
print('Квадратный корень = ', guess)
