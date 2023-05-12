###1
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
# b = []
# for i in range(len(subject_marks)):
#     a = subject_marks[i][0] + ' ' + str(subject_marks[i][1])
#     b.append(a)
# print(*sorted(b, key=lambda x: int(x.split()[1])), sep='\n')
####
# [print(*i) for i in sorted(subject_marks, key=lambda x: x[1])]

# ###2
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# [print(*i) for i in sorted(subject_marks, key=lambda x: -x[1])]

####3
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# [print(*i) for i in sorted(subject_marks, key=lambda x: (-x[1], x[0]))]

###4
# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
# models_sort = sorted(models, key=lambda x: x['color'])
# for i in models_sort:
#     print(f'Производитель: {i["make"]}, модель: {i["model"]}, цвет: {i["color"]}')

###5
# s = input()
# c = {}
# while s != 'конец':
#     b = s.split(':')
#     a = {b[0]: int(b[1])}
#     c.update(a)
#
#     s = input()
# for k, v in sorted(c.items(),key=lambda x: -x[1]):
#     print(k)

####6
# n = int(input())
# oskar = {}
# name_actor = [input() for _ in range(n)]
# for i in name_actor:
#     oskar[i] = oskar.get(i, 0) + 1
# oskar_sort = sorted(oskar.items(), key=lambda x: -x[1])
# print(oskar_sort)
# print(f'{oskar_sort[0][0]}, {oskar_sort[0][1]}')
# print(f'{oskar_sort[-1][0]}, {oskar_sort[-1][1]}')
# ####
# d = {}
# for _ in range(int(input())):
#     e = input()
#     d[e] = d.get(e, 0) + 1
# kmax, kmin = max(d, key=d.get), min(d, key=d.get)
# print(kmax, d[kmax], sep=', ')
# print(kmin, d[kmin], sep=', ')
###7 Телефонная книга
# pb = {}
# for _ in range(int(input())):
#     num, name = input().split()
#     pb[name] = pb.get(name, []) + [num]
# [print(*pb.get(input(), ['Неизвестный номер'])) for _ in range(int(input()))]

###8 Дни рождения
# n = int(input())
# word = {}
#
# for i in range(n):
#     s = input().split()
#     name = s[0]
#     opis = s[-1]
#     word[opis] = word.get(opis, []) + [name]
# print(word)
#
# m = int(input())
# for i in range(m):
#     aa = input()
#     if aa in word:
#         print(*sorted(word[aa]))
#     else:
#         print('Нет данных')

###9 Рейтинг таксисt
# tax = {}
# s = input()
# while s != '':
#     b = s.split(', ')
#     tax[b[0]] = tax.get(b[0], []) + [int(b[1])]
#     s = input()
# print(tax)
#
# for k, v in tax.items():
#     tax[k] = sum(v) / len(v)
# print(tax)
#
# for a, b in sorted(tax.items(), key=lambda x: (-x[1], x[0])):
#     print(a, b)

###10 Дили Вили Били
coment = {'Дили': [], 'Били': [], 'Вили': []}
s = input()
while s != "":
    a = s.split(': ')
    for i in coment:
        if i == a[0]:
            coment[a[0]] = coment.get(a[0], []) + [a[1]]
        # coment.setdefault(a[0], []).append(a[1])
    s = input()
print(coment)

for k, v in coment.items():
    coment[k] = len(set(v))
print(coment)

for a, b in sorted(coment.items(), key=lambda x: -x[1]):
    print(f'Количество уникальных комментаторов у {a} - {b}')
