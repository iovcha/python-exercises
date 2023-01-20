#milles1 = 1.6  # km
#gallon1 = 3.79  #litr
#a = float(input('Сколько миль вы проехали? '))
#b = float(input('Сколько галлон вы использовали? '))
#print('Вы проехали:', a * 1.6,'km', 'Вы использовали: %.2f' % (b * 3.79),'litr')

m1 = 1
m2 = 5
m3 = 10
m4 = 25
loonie = 100
toonie = 200
cents = int(input('Ваша сдача в центах: '))
s1 = cents // toonie
print('Ваша сдача:',s1,"toonie")
cents = cents % toonie
s2 = cents//loonie
print('Ваша сдача:',s2, "loonie")
cents = cents % loonie
s3 = cents//m4
print('Ваша сдача:', s3," цента по 10")
cents = cents % m4
s4 = cents // m3
print('Ваша сдача:',s4,"цента по 25")
cents = cents % m3
s5 = cents // m2
print('Ваша сдача:', s5, "цента по 5")
cents = cents % m2
s6 = cents // m1
print('Ваша сдача:',s6, "цента по 1/")







