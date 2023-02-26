def factor(n):
    f = 1
    for i in range(1, (n + 1)):
        f *= i
    return f
res = factor(5)
print(res)


