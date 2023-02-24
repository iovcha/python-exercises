#1.	Преобразуйте матрицу A(n, m) таким образом,
# чтобы строки с нечетными индексами были упорядочены по убыванию, а с четными - по возрастанию.

#matrix =[[1, 8, 3, 2],
#         [7, 4, 1, 10],
#         [4, 1, 0, 8],
#         [4, 9, 1, 12]]
#for i in range(0, len(matrix)):
#    if i % 2 == 0:
#        matrix[i].sort()
#    elif i % 2 != 0:
#        matrix[i].sort(reverse=True)
#print(matrix)

#2.	Дана квадратная матрица. Проверьте, является ли она диагональной.
#matrix =[[3, 0, 0],
#         [0, 3, 0],
#         [0, 0, 5]]
#flag = False
#for i in range(0, len(matrix)):
#    for j in range(0, len(matrix[i])):
#        elem = matrix[i][j]
#        if (i > j) and elem != 0:
#            flag = True
#            break
#        elif (i < j) and elem != 0:
#            flag = True
#            break
#if flag == True:
#    print("является не диагональной.")
#else:
#    print("является  диагональной.")

#3.	Дана квадратная матрица. Проверьте, является ли она нижнетреугольной.
# Если да, преобразуйте ее таким образом, чтобы она стала верхнетреугольной.

matrix = [[5, 0, 0, 0],
          [8, 2, 0, 0],
          [5, 3, 9, 0],
          [5, 2, 1, 8]]


transposed_matrix = []
flag = False


for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        elem = matrix[i][j]
        if (i < j) and elem != 0:
            flag = True
            break

if flag == True:
    print("не является  нижнетреугольной")
else:
    print("является  нижнетреугольной")


for j in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[j])
    transposed_matrix.append(transposed_row)
print(transposed_matrix)
