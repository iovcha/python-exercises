# Запрашиваем у пользователя год
year = int(input("Введите год: "))
# Определяем, високосный или нет
if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False
# Отображаем результат
if isLeapYear:
    print(year, " – високосный год.")
else:
    print(year, " – невисокосный год.")
