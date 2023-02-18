#1
#matrix = [[2, -4, 6, -8],
#          [4, 3, 1, 2],
#          [-5, -1, 3, 10]]
#max_elem = matrix[0][0]
#min_elem = matrix[0][0]
#i_max = j_max = i_min = j_min = 0
#for i in range(0, len(matrix)):
 #   for j in range(0, len(matrix[i])):
 #       if matrix[i][j] > max_elem:
 #           max_elem = matrix[i][j]
#            i_max = i
 #           j_max = j
 #       elif matrix[i][j] < min_elem:
 #           min_elem = matrix[i][j]
 #           i_min = i
 #           j_min = j
 #       matrix[i_min][j_min], matrix[i_max][j_max] = matrix[i_max][j_max], matrix[i_min][j_min]

#print(max_elem, i_max, j_max)
#print(min_elem,i_min, j_min)
#print(matrix)

#2.	Дана квадратная матрица. Проверьте, является ли она единичной.
#matrix = [[1, 0, 0],
#          [0, 1, 0],
#          [9, 0, 1]]

#flag = False
#for i in range(0, len(matrix)):
#    for j in range(0, len(matrix[i])):
 #       elm = matrix[i][j]
 #       if (i == j and elm != 1) or (i != j and elm != 0):
 #           flag = True
 #           break
#if flag == True:
#    print('Матрица  не единичная')
#else:
#    print('Матрица  единичная')

 #3.	Преобразуйте исходную матрицу A(n,m) так,
# чтобы первый элемент в каждой ее строке был заменен на среднее арифметическое элементов этой строки.

#matrix = [[4, 7, 10],
#          [3, 2, 1],
#          [5, 7, 1]]
#for i in range(0, len(matrix)):
#    for j in range(0, len(matrix[i])):
#        elm = matrix[i][j]
#        a = matrix[0]
#        arith_mean1 = sum(a) / (len(matrix[0]))
#        matrix[0][0] = int(arith_mean1)
#        b = matrix[1]
#        arith_mean2 = sum(b) / (len(matrix[1]))
#        matrix[1][0] = int(arith_mean2)
#        c = matrix[2]
#        arith_mean3 = sum(c) / (len(matrix[2]))
#        matrix[2][0] = int(arith_mean3)
#print('%d , %d, %d' % (arith_mean1, arith_mean2, arith_mean3))
#print(matrix)

#4.	Дана квадратная матрица. Проверьте, является ли она верхнетреугольной.

#matr = [[4, 7, 10],
#        [0, 2, 1],
 #       [0, 0, 1]]
#flag = False
#for i in range(0, len(matr)):
#    for j in range(0, len(matr[i])):
#        elmem = matr[i][j]
#        if (i > j) and elmem != 0:
#            flag = True
 #           break
#if flag == True:
#    print("Матрмца не является верхнетреугольной ")
#else:
#    print("Матрмца  является верхнетреугольной")

#5.	Дана квадратная матрица. Проверьте, является ли она симметричной.

matr = [[2, 1, -2],
        [1, 0, 3],
        [-2, 3, -4]]
transposed_matr = []
flag = False
for j in range(len(matr[0])):
    transposed_row = []
    for row in matr:
        transposed_row.append(row[j])
    transposed_matr.append(transposed_row)
    if transposed_matr == matr:
        flag = True
        break
if flag == True:
    print("Матрмца  является симметричной")
else:
    print("Матрмца не является симметричной ")
















