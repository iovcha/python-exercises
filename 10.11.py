string = input()
a = []
for i in string:
    if i in "0123456789":
        a.append(int(i))
print(len(a), sum(a))