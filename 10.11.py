string = input()
a = []
for i in range(len(string)):
    if string[i] == '(':
        a.append(string[i])
        continue
    if string[i] == ')' and a:
        if (a[-1] + string[i] == '()'):
            a.pop()
    else:
        a.append(string[i])
if a == []:
    print('YES')
else:
    print('NO')


