string = input()
bracket_open = ['(', '[', '{']
bracket_closed = [')', ']', '}']
a = []
for i in range(len(string)):
    if string[i] in bracket_open:
        a.append(string[i])
        continue
    if string[i] in bracket_closed and a:
        if (a[-1] + string[i] == '()') or (a[-1] + string[i] == '[]') or (a[-1] + string[i] == '{}') :
            a.pop()
    else:
        a.append(string[i])
if a == []:
    print('YES')
else:
    print('NO')


