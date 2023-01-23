#Китайский гороскоп
year = int(input('Ваш год рождения : '))
if year % 12 == 8:
    animals = 'Дракон'
elif year % 12 == 9:
    animals = "Змея"
elif year % 12 == 10:
    animals = "Лошадь"
elif year % 12 == 11:
    animals = "Коза"
elif year % 12 == 0:
    animals = "Обезьяна"
elif year % 12 == 1:
    animals = "Петух"
elif year % 12 == 2:
    animals = "Собака"
elif year % 12 == 3:
    animals = "Свинья"
elif year % 12 == 4:
    animals = "Крыса"
elif year % 12 == 5:
    animals = "Бык"
elif year % 12 == 6:
    animals = "Тигр"
else:
    animals = "Кролик"
print("Вы родились в год ", animals)
