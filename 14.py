#. Шкала Рихтера
magnitude = float(input("Введите магнитуду землетрясения по шкале Рихтера : "))
if magnitude < 2.0:
    earthquakes = 'минемальное'
elif 2.0 <= magnitude < 3.0:
    earthquakes = 'очень слабое'
elif 3.0 <= magnitude < 4.0:
    earthquakes = 'слабое'
elif 4.0 <= magnitude < 5.0:
    earthquakes = 'промежуточное'
elif 5.0 <= magnitude < 6.0:
    earthquakes = 'умеренное'
elif 6.0 <= magnitude < 7.0:
    earthquakes = 'сильное'
elif 7.0 <= magnitude < 8.0:
    earthquakes = 'очень сильное'
elif 8.0 <= magnitude < 10.0:
    earthquakes = 'огромное'
else:
    earthquakes = 'разрушительное'
print('этой магнитуде соответствует', earthquakes,'землетрясения')
