# n = int(input())
# a = 0
# k = 0
# for i in range((n + 1), n * 2):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             a += 1
#     if a == 0:
#         k += 1
#     a = 0
# print(k)


# Пузырьковая сортировка
# n = int(input())
# lst = list(map(int, input().split()))
# k = 0
#
# for j in range(0, n - 1):
#     flag = False
#     for i in range(1, len(lst)):
#         if lst[i - 1] > lst[i]:
#             lst[i - 1], lst[i] = lst[i], lst[i - 1]
#             k += 1
#             flag = True
#     if not flag:
#         break
# print(*lst, '\n' + str(k))


#Система уравнений
# n, m = map(int, input().split())
# count = 0
# for a in range( 1001):
#     for b in range( 1001):
#         if a ** 2 + b == n and a + b ** 2 == m:
#             count += 1
# print(count)

#Сортировка вставками
n = int(input())
lst = list(map(int, input().split()))
print(lst)
for i in range(n - 1):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(*lst)