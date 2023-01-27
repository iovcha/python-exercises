#. Числовые оценки – в буквенные
#. Сейчас перевернем ситуацию и  попробуем определить
#буквенный номинал оценки по его числовому эквиваленту. Убедитесь
#в том, что ваша программа будет обрабатывать числовые значения между
#указанными в табл. 2.13. В этом случае оценки должны быть округлены до
#ближайшей буквы. Программа должна выдавать оценку A+, если введенное пользователем значение будет 4,0 и выше
#Буквенная оценка Числовая оценка
#A+ 4,0 C+ 2,3
#A 4,0 C 2,0
#A- 3,7 C- 1,7
#B+ 3,3 D+ 1,3
#B 3,0 D 1,0
#B- 2,7 F 0
grade_num = float(input("Ваша  оценка  в числовом эквиваленте : "))
if grade_num > 4.0:
    grade_letter = "A+"
elif grade_num == 4.0:
    grade_letter = "A"
elif grade_num < 4 and grade_num >= 3.7:
    grade_letter = "A-"
elif grade_num < 3.7 and grade_num >= 3.3:
    grade_letter = "B+"
elif grade_num < 3.3 and  grade_num >= 3.0:
    grade_letter = "B"
elif grade_num < 3.0 and grade_num >= 2.7:
    grade_letter = "B-"
elif grade_num < 2.7 and grade_num >= 2.3:
    grade_letter = "C+"
elif grade_num < 2.3 and grade_num >= 2.0:
    grade_letter = "C"
elif grade_num < 2.0  and grade_num >= 1.7:
    grade_letter = "C-"
elif grade_num >= 1.3 and grade_num < 1.7:
    grade_letter = "D+"
elif  grade_num >= 1.0 and grade_num < 1.7:
    grade_letter = "D"
elif grade_num == 0:
    grade_letter = "F"
else:
    grade_letter = "ERROR"
print("Вашей оценке в числовом эквиваленте %.1f. " % grade_num, "соотыетствует", grade_letter, " в буквенном эквиваленте")





