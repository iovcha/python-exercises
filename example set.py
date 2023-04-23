# Девушка или Юноша
# name = list(input())
# l = len(set(name))
# if l % 2== 0:
#     print('CHAT WITH HER!')
# else:
#     print('IGNORE HIM!')

###2  Не смешите мои подковы
# a = list(map(int, input().split()))

# l1 = len(a)
# l2 = len(set(a))
# print(l1 - l2)

###3 Панграмма
# lst = list(input().lower())
# if len(set(lst))== 26:
#     print('YES')
# else:
#     print('NO')

###4 Красивый год
# year = int(input())
# while True:
#     year += 1
#     if len(set(str(year))) == 4:
#         print(year)
#         break

####5 Антон и буквы
# letters = input()
# a = {i for i in letters if i.isalpha()}
# print(len(a)

###6
# words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
#          'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
#          'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
#          'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
#          'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
#          'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
#          'control', 'value', 'few', 'generation', 'service', 'national',
#          'tradition', 'government', 'mention', 'proposal']
# words_set= {word for word in words if len(word)> 6}
# print(len(words_set))

#####7
# n = int(input())
# for _ in range(n):
#     lst = set(list(map(int, input().split())))
#     print(len(lst))

#####8
# lst_set = set()
# for _ in range(int(input())):
#     lst = list(map(int, input().split()))
#     lst_set.update(lst)
# print(len(lst_set))

####9
# phraza = input().lower().split(',')
# lst = set()
#
# for i in phraza:
#     if i not in lst:
#         print('НЕТ')
#         lst.add(i)
#     else:
#         print('ДА')

###10
# s1  = list(map(int,input().split()))
# s2 = list(map(int,input().split()))
# s1_s2 = set(s1).intersection(s2)
# print(*(sorted(s1_s2)))

###11
# s1  = list(map(int,input().split()))
# s2 = list(map(int,input().split()))
# print(*(sorted(set(s1).difference(set(s2)))))

###12
# lst = input()
# lst_set = set()
# for i in  lst:
#     if i.isdigit() and lst.count(i) > 1:
#         lst_set.add(i)
# if len(lst_set)>= 1:
#     print(*(sorted(lst_set)))
# else:
#     print('No')
###13
# s = input()
# s_set = []
# for i in s:
#     if i not in s_set:
#         s_set.append(i)
# print(''.join(map(str, s_set)))

###14
# my_frozen = frozenset()
# s = '7'
# lst = []
# for i in range(int(input())):
#     a = s + s * i
#     lst.append(int(a))
#     my_frozen = frozenset(lst)

###15
# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
#          'drop', 'produce', 'acquisition', 'cheap', 'strength',
#          'master', 'perception', 'noise', 'strange', 'am']
# a = []
# for index, value in enumerate(words, 1):
#     words_with_position = (value, index)
#     a.append(words_with_position)
# print(a)

###16
# english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
#                  'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
#                  'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
#                  'ask', 'go', 'suggest')
# for number, word in enumerate(english_words, 1):
#     print(f'Word № {number} = {word}')

###17 Алгоритм Луна
n = str(input())
a = []
for i, j in enumerate(n):
    if i % 2 == 1:
        a.append(int(j))
    elif i % 2 == 0 and int(j) * 2 < 9:
        a.append(int(j) * 2)
    else:
        a.append(abs(int(j) * 2 - 9))
print(sum(a) % 10 == 0)
#######print(sum([v if k%2 == 0 else v*2 if v*2 < 9 else v*2 - 9
           #for k, v in enumerate(map(int, input()), 1)])%10 == 0)#в одну строку