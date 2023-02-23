#1.	Дана строка, представляющая из себя некоторое выражение. Проверить корректность использования скобок в заданном выражении:
#a.	количество открывающихся скобок каждого вида должно соответствовать количеству закрывающихся скобок этого же вида;
#b.	порядок следования открывающихся и закрывающихся скобок должен быть верным.
l = "aaa(bc{def}(ggg(hh))"
a = []
braces = {']': '[', '}': '{', ')': '('}
for i in l:
    if i in braces.values():
      a.append(i)
    elif i in braces.keys():
        if len(a) > 0 and braces[i] == a[-1]:
            a.pop()
        else:
            print("Выражение неправильное")
            break
else:
     print("Выражение правильное")

#2.	Вычислить произведение последних трех чисел не кратных 5 в диапазоне от 20 до 50.
lst = []
for i in range(20, 51):
    if i % 5 != 0:
       lst.append(i)
print(int(lst[-3] * lst[-2] * lst[-1]))

#3.	Найти 2-ое, 6-ое и 11-ое по счету числа кратные 7, но не кратные 13 в диапазоне от 1000 до 2000.
lst = []
for i in range(1000, 2001):
    if i % 7 == 0 and i % 13 != 0:
        lst.append(i)
print(lst[1], lst[5], lst[10])