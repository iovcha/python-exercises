#Буквенная оценка Числовая оценка Буквенная оценка Числовая оценка
#A+ 4,0 C+ 2,3
#A 4,0 C 2,0
#A- 3,7 C- 1,7
#B+ 3,3 D+ 1,3
#B 3,0 D 1,0
#B- 2,7 F
grade_letter = input("Ведите оценку в буквенном выражении: ")
grade_letter = grade_letter.upper()
sum_grade = 0
grade_num = 0
sp = []
count = 0
while grade_letter != "":
    count += 1
    if grade_letter == "A" or grade_letter == "A+":
        grade_num = 4.0
    elif grade_letter == "A-":
        grade_num = 3.7
    elif grade_letter == "B+":
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
    else:
        grade_num = "invalid"
    if grade_num == "invalid":
        print(("Введена некорректная оценка."))
    else:
        print("Буквенная оценка", grade_letter, "соответствует", grade_num, "баллам.")
    sp.append(grade_num)
    print(sp)
    grade_letter = input("Ведите оценку в буквенном выражении: ")
    grade_letter = grade_letter.upper()
print(count)
print(sum(sp))
print("Средяя оценка: %.2f" % (sum(sp) / count))





