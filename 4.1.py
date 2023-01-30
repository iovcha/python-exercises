#. Следующий день
day = int(input("Введите день: "))
month = str(input("Введите месяц : "))
year = int(input("Ваедите год: "))
if day == 31 and month == "декабря":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 января ",(year + 1),"года")
elif day == 30 and month == "апреля":
    print(day, month, year, "года. Дата, следующуя за вашей это 1 мая", year, "года")
elif day == 30 and month == "июня":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 июля", year, "года")
elif day == 30 and month == "сентября":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 октября", year, "года")
elif day == 30 and month == "ноября":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 декабря", year, "года")
elif day == 31 and month == "января":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 февраля", year, "года")
elif day == 31 and month == "марта":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 апреля", year, "года")
elif day == 31 and month == "мая":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 июня", year, "года")
elif day == 31 and month == "июля":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 августа", year, "года")
elif day == 31 and month == "августа":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 сентября", year, "года")
elif day == 31 and month == "октября":
    print(day, month, year, " года. Дата, следующуя за вашей это 1 ноября", year, "года")
elif day == 28 and month == "февраля" and year % 4 != 0 or day == 29 and month == "февраля" and year % 4 == 0:
    print(day, month, year, " года. Дата, следующуя за вашей это 1 марта ", year, "года")
elif day > 31 and month in ("января", "марта", "мая", "июля", "августа", "октября", "декабря"):
    print("Не корректно введена дата")
elif day > 30 and month in ("апреля", "июня", "сентября", "ноября"):
    print("Не корректно введена дата")
elif day > 28 and month == "февраля" and year % 4 != 0 or day >29 and month == "февраля" and year % 4 == 0:
    print("Не корректно введена дата")
else:
    print(day, month, year, " года. Дата, следующуя за вашей это ", (day + 1), month, year, "года")
