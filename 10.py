n = int(input())
for i in range(n):
    word = input().lower()
    ind = word.find('рок') + 1
    if ind > 0:
       print(i + 1, ind)



