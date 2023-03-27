n = str(input())
sum1 = 0
sum2 = 0
for i in range(len(n)):
    if i % 2 == 0:
        sum1 += int(n[i])
    elif i % 2 == 1:
        sum2 += int(n[i])
if (sum1 - sum2) % 11 == 0:
    print("YES")
else:
    print("NO")





