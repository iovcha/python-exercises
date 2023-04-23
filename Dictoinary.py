# lst = input().lower()
# d = {}
# for i in lst:
#     if i.isalpha():
#         d[i]= d.get(i, 0) + 1
# print(d)

###2Во сколько обойдется данная покупка? Хотим купить все товары в указанном количестве
# supermarket = {
#     "milk": {"quantity": 20, "price": 1.19},
#     "biscuits": {"quantity": 32, "price": 1.45},
#     "butter": {"quantity": 20, "price": 2.29},
#     "cheese": {"quantity": 15, "price": 1.90},
#     "bread": {"quantity": 15, "price": 2.59},
#     "cookies": {"quantity": 20, "price": 4.99},
#     "yogurt": {"quantity": 18, "price": 3.65},
#     "apples": {"quantity": 35, "price": 3.15},
#     "oranges": {"quantity": 40, "price": 0.99},
#     "bananas": {"quantity": 23, "price": 1.29}
# }
# a = []
# for key in supermarket:
#     #n = supermarket[key]["quantity"] * supermarket[key]["price"]
#     n = (supermarket.get(key).get("quantity") * supermarket.get(key).get("price"))
#     a.append(n)
# print(round(sum(a), 2))

###3 Анаграмма
# s1,s2 = input(), input()
# d1,d2 = {}, {}
#
# for i in s1:
#     d1[i] = d1.get(i, 0) + 1
#
# for j in s2:
#     d2[j] = d2.get(j, 0) + 1
#
# if d1 == d2:
#     print("YES")
# else:
#     print("NO")

#####
# cnt = {}
# for ch in input():
#     cnt[ch] = cnt.get(ch, 0) + 1
# for ch in input():
#     cnt[ch] = cnt.get(ch, 0) - 1
#     if cnt[ch] < 0:
#         print('NO')
#         break
# else:
#     print('YES')####print(('YES', 'NO')[any(cnt.values())])

##4 Азбука Морзе
# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••'}
# phraza = input().lower().split()#####for i in input().lower().split():
#                                           #print(*[morze[j] for j in i]
# for i in phraza:
#     for x in i:
#         morze[x] = morze.get(x)
#         print(morze[x], end=' ')
#     print()

###5
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
# data = {}
# for i in persons:
#     key = ['salary', 'gender', 'passport']
#     data[i[0]] = dict(zip(key,i[1:]))
# print(data)

####6
# from pprint import pprint
# data = {
#     "my_friends": {
#         "count": 10,
#         "people": [{
#             "first_name": "Kurt",
#             "id": 621547005,
#             "last_name": "Cobain",
#             "bdate": "31.8.2005"
#         }, {
#             "first_name": "Виолетта",
#             "id": 484200150,
#             "last_name": "Кастилио",
#         }, {
#             "first_name": "Иринка",
#             "id": 21886133,
#             "last_name": "Бушуева",
#             "bdate": "28.8.1942"
#         }, {
#             "first_name": "Данил",
#             "id": 282456573,
#             "last_name": "Греков",
#             "bdate": "4.7.2002"
#         }, {
#             "first_name": "Валентин",
#             "id": 184902932,
#             "last_name": "Долматов",
#             "bdate": "25.5"
#         }, {
#             "first_name": "Евгений",
#             "id": 620469646,
#             "last_name": "Шапорин",
#             "bdate": "6.12.1982"
#         }, {
#             "first_name": "Ангелина",
#             "id": 622328862,
#             "last_name": "Краснова",
#             "bdate": "4.11.1995"
#         }, {
#             "first_name": "Иван",
#             "id": 576015198,
#             "last_name": "Вирин",
#             "bdate": "2.2.1915"
#         }, {
#             "first_name": "Паша",
#             "id": 386922406,
#             "last_name": "Воронов",
#             "bdate": "27.9"
#         }, {
#             "first_name": "Ольга",
#             "id": 622170942,
#             "last_name": "Савченкова",
#             "bdate": "20.12"
#         }]
#     }
# }
# x = data['my_friends']['people']
# a = []
# for i in range(len(x)):
#     a.append(x[i]['first_name'])
#     a.sort()
# print(*a,sep='\n')

# pprint(len(data['my_friends']['people']))
# pprint(data['my_friends']['people'])

###1
# from pprint import pprint
# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17",
#     "employment": {
#         "title": "Central Hospitality Liaison",
#         "key_skill": "Organisation"
#     },
#     "subscription": {
#         "plan": "Essential",
#         "status": "Idle",
#         "payment_method": "Debit card",
#         "term": "Annual"
#     }
# }
# a = input().split()
# new_user = {key: user[key] for key in a }
# print(new_user)

####2
# people = [
#     ['Amy Smith', '694.322.8133x22426'],
#     ['Brian Shaw', '593.662.5217x338'],
#     ['Christian Sharp', '118.197.8810'],
#     ['Sean Schmidt', '9722527521'],
#     ['Thomas Long', '163.814.9938'],
#     ['Joshua Willis', '+1-978-530-6971x601'],
#     ['Ann Hoffman', '434.104.4302'],
#     ['John Leonard', '(956)182-8435'],
#     ['Daniel Ross', '870-365-8303x416'],
#     ['Jacqueline Moon', '+1-757-865-4488x652'],
#     ['Gregory Baker', '705-576-1122'],
#     ['Michael Spencer', '(922)816-0599x7007'],
#     ['Austin Vazquez', '399-813-8599'],
#     ['Chad Delgado', '979.908.8506x886'],
#     ['Jonathan Gilbert', '9577853541']
# ]
# # for i in people:
# #     print(i)
# phone_book = {i[1]: i[0] for i in people}
# print(phone_book)

####3
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# for i in vector:
#     #print(i)
#     for j in range(len(i)):
#         print(i[j], end=' ')
vector2 = [i[j] for i in vector for j in range(len(i))]
print(vector2)


