# 1посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.
# n = int(input())
# matrix = []
# s = 0
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             s += matrix[i][j]
# print(s)

# еще одно решение
# res = 0
# for i in range(int(input())):
#     res += int(input().split()[i])
# print(res)

# 2Обход элементов матрицы - 1
# matrix = []
# n = int(input())
# ###a = [list(map(int, input().split())) for _ in range(n)] так можно сделать матрицу квадратную
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# for j in range(n):
#     for i in range(n):
#         print(matrix[j][i], end=' ')
#     print()

# 3 Обход элементов матрицы - 2
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n - 1, -1, -1):
#     for j in range(n - 1, -1, -1):
#         print(matrix[j][i], end=' ')
#     print()

# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n) ]
# print(matrix)
# for j in range(n):
#     for i in range(m-1, -1, -1):
#         print(matrix[j][i], end=' ')
#     print()

# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n) ]
# for i in range(n-1, -1, -1):
#     for j in range(m):
#         print(matrix[i][j], end=" ")
#     print()

# 4 A. Красивая матрица
# a = [[int(x) for x in input().split()] for y in range(5)]
# for i in range(5):
#     for j in range(5):
#         if a[i][j] == 1:
#             print(abs(i - 2) + abs(j - 2))

# 5 Сумма строк и столбцов двумерного массива
# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for i in range(n):
#     summa_row = 0  # строка
#     for j in range(m):
#         summa_row += matrix[i][j]
#     print(summa_row, end=' ')
#
# print('')
#
# # for j in range(m):
#     summa_column = 0  # столбец
#     for i in range(n):
#         summa_column += matrix[i][j]
#     print(summa_column, end=' ')
# 5.1 ##еще одно решение
# n, m = map(int, input().split())
# x = [[int(k) for k in input().split()] for i in range(n)]  # [[5, 9, 2, 6], [6, 2, 4, 3], [1, 2, 8, 7]]
# x_columns = list(zip(*x))  # [(5, 6, 1), (9, 2, 2), (2, 4, 8), (6, 3, 7)]# получение столбца!!!
# for a in x:
#     print(sum(a), end=' ')
# print()
# for b in x_columns:
#     print(sum(b), end=' ')


# 6 Симметричная ли матрица?
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# for i in a:
#     print(i)
# flag = True
# for i in range(n):
#     for j in range(n):
#         if a[i][j] != a[j][i]:
#             flag = False
#             break
# if flag:
#     print('Yes')
# else:
#     print('No')

# 7 Состязания
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
#
# b = []
# for i in range(n):
#     summa_row = 0
#     for j in range(m):
#         summa_row += a[i][j]
#     b.append(summa_row)
# print(max(b), b.index(max(b)), sep='\n')
# a = [sum([int(i) for i in input().split()]) for j in range(n)]

# 7.1
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# max_elem = 0
# i_max = 0
# j_max = 0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] > max_elem:
#             max_elem = a[i][j]
#             i_max = i
#             j_max = j
# print(i_max, j_max, end=' ')
#
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
#
# b = [max(i) for i in a]
# print(b)
# print(max(b))
# print(b.index(max(b)), a[b.index(max(b))].index(max(b)))
# print(a[b.index(max(b))])

# 8 Состязания - 3
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# b = []
#
# mx_elem = 0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] > mx_elem:
#             mx_elem = a[i][j]
#
# for i in range(n):
#     if mx_elem in a[i]:
#         b.append(sum(a[i]))
#         print(b)
#     else:
#         b.append(0)
# print(b.index(max(b)))

##9 Состязания - 4
# n, m = map(int, input().split())
# #matrix = [list(map(int, input().split())) for _ in range(n)]
# a = []
# for i in [list(map(int, input().split())) for _ in range(n)]:
#     a.append(max(i))
# print(a)
# print(a.count(max(a)))

##10 Симпатичный узор
# n = 4
# a = [input().upper() for _ in range(n)]
# print(a)
# flag = True
# for i in range(n - 1):
#     for j in range(n - 1):
#         if a[i][j] + a[i][j + 1] == a[i + 1][j] + a[i + 1][j + 1]:
#             flag = False
# if flag:
#     print('Yes')
# else:
#     print('No')

# 11 Миша и негатив
# n, m = map(int, input().split())
# a = [input().upper() for _ in range(n)]
# input()
# b = [input().upper() for _ in range(n)]
#
#
# count = 0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == b[i][j]:
#             count += 1
# print(count)
##12 A. Таблица умножения
n, x = map(int, input().split())
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == x:
            count += 1
print(count)
