#0. На какой день недели выпадает 1 января?
year = int(input("Введите год: "))
from math import floor
day_of_the_week = (year + floor((year - 1)/4) - floor((year - 1)/100) + floor((year - 1)/400)) % 7
if day_of_the_week == 0:
    name = "воскресенье"
elif day_of_the_week == 1:
    name = "понедельник"
elif day_of_the_week == 2:
    name = "вторник"
elif day_of_the_week == 3:
    name = "среда"
elif day_of_the_week == 4:
    name = "четверг"
elif day_of_the_week == 5:
    name = "пятницу"
else:
    name = "субботу"
print("1 января", year, " года приходиться на",name)

