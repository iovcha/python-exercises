# 1 Побочная диагональ
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# b = [a[i][n-i-1] for i in range(n)]
# print(max(b))

# 2 Заполнение матрицы
# mtrx = []
# n = int(input())
# a, b, c = map(int, input().split())
# for i in range(n):
#     mtrx.append([0] * n)
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             mtrx[i][j] = c
#         elif i > j:
#             mtrx[i][j] = b
#         else:
#             mtrx[i][j] = a
#
# for i in mtrx:
#     print(*i)

##3 A. Матчи

# n = int(input())
# b = [list(map(int, input().split())) for _ in range(n)]
# count = 0
#
# for i in range(n):
#     for j in range(n):
#         if b[i][0] == b[j][1]:
#             count += 1
# print(count)

##4 Морской бой - 2
# n, m = map(int, input().split())
# mtrx = []
# mtrx.append('.' * (m + 2))
# for i in range(n):
#     row = '.' + input() + '.'
#     mtrx.append(row)
# mtrx.append('.' * (m + 2))
# count = 0
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if mtrx[i-1][j] == '.' and mtrx[i][j + 1] == '.' and mtrx[i+1][j] == '.' and mtrx[i][j-1] == '.'\
#                 and mtrx[i][j] == '.':
#             count += 1
# print(count)

##5 Заполнение соседями
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
#
# for i in range(1, n):
#     for j in range(1, m):
#         matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
#
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()

##6 Заполнение соседями-2
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
#
# for i in range(n - 2, -1, -1):
#     for j in range(m - 2, -1, -1):
#         matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]
#
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()

##7 Заполнение змейкой
# n, m = map(int, input().split())
# k = 0
# for i in range(n):
#     a = []
#     for j in range(m):
#         a.append(k)
#         k += 1
#     #print(*a)
#     if i % 2 == 1:
#         a.reverse()
#     if i == 0:
#         print(*a, sep=2*" ")
#     else:
#         print(*a)

##еще одно решение
# n, m=map(int, input().split())
# for i in range(n):
#     a=[j for j in range(m*i, m+m*i)]
#     if i%2 !=0:
#         a.reverse()
#     print(*a)

###8 A. Фотографии Брейна
# n, m = map(int,input().split())
# a = [list(input().upper().split()) for _ in range(n)]
# k = 0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] in 'WBG':
#             k += 1
#         else:
#             k -= 1
# if k == (n * m ):
#     print("#Black&White")
# else:
#     print("#Color")
##еще одно решение
# n, m = map(int, input().split())
# a = [list(input().upper().split()) for _ in range(n)]
# f = "#Black&White"
# for i in range(n):
#     for j in range(m):
#         if a[i][j] not in "WBG":
#             f = "#Color"
#             break
# print(f)

###9 Спираль
# n = int(input())
# a = [[0] * n for i in range(n)]
# count = 0
# for i in range(n):
#     count += 1
#     a[0][i] = count
# i = 0  # указываем последнюю заполненную ячейку
# j = n - 1
# n -= 1  # устанавливаем размер 1 блока 1 витка
# while len(a) ** 2 != count:
#     for k in range(n):  # движение вниз
#         i += 1
#         count += 1
#         a[i][j] = count
#     for k in range(n):  # движение влево
#         j -= 1
#         count += 1
#         a[i][j] = count
#     for k in range(n - 1):  #движение вверх
#         i -= 1
#         count += 1
#         a[i][j] = count
#     for k in range(n - 1): #движение вправо
#         j += 1
#         count += 1
#         a[i][j] = count
#     n -= 2  # обеспечиваем переход на внутренний виток
#
# for i in range(len(a)):  # вывод полученной матрицы
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

##10 A. Тортминатор
r, c = map(int, input().split())
a = [input().upper() for _ in range(r)]
# count_row = 0
# count_column = 0
#
# for i in range(r):  # движение по строкам
#     if 'S' not in a[i]:
#         count_row += 1
#
# for j in range(c):  # движение по столбцам
#     b = [column[j] for column in a]
#     if 'S' not in b:
#         count_column += 1
# print(count_row * c + count_column * (r - count_row))
###print(list(zip(*a))) получение столбца