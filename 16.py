#Буквенные оценки – в числовые
#Таблица 2.13. Оценка успеваемости
#Буквенная оценка Числовая оценка Буквенная оценка Числовая оценка
#A+ 4,0 C+ 2,3
#A 4,0 C 2,0
#A- 3,7 C- 1,7
#B+ 3,3 D+ 1,3
#B 3,0 D 1,0
#B- 2,7 F 0
grade_letter = str(input('Введите буквенную оценку: '))
grade_letter = grade_letter.upper()
grade_num = ""
if grade_letter == "A" or grade_letter == "A +":
    grade_num = 4.0
elif grade_letter == "A-":
    grade_num = 3.7
elif  grade_letter == "B+":
    grade_num = 3.3
elif grade_letter == "B":
    grade_num = 3.0
elif grade_letter == "B-":
    grade_num = 2.7
elif grade_letter == "C+":
    grade_num = 2.3
elif grade_letter == "C":
    grade_num = 2.0
elif grade_letter == "C-":
    grade_num = 1.7
elif grade_letter == "D+":
    grade_num = 1.3
elif grade_letter == "D":
    grade_num = 1.0
elif grade_letter == "F":
    grade_num = 0
if grade_num == "":
    print("ERROR")
else:
     print("Буквенной оценке", grade_letter,"соответствует оцeнка в числовом выражении", grade_num)

