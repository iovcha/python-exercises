#1.	1.	Дан словарь {‘v’: ‘s001’, ‘v1’: ‘s002’, ‘v2’: ‘s001’, ‘v3’: ‘s005’, ‘v4’: ‘s005’, ‘v5’: ‘s009’, ‘v6’: ‘s007’}.
# Выведите на экран все значения словаря таким образом, чтобы ни одно из них не повторялось.

#dic = {'v': 's001', 'v1': 's002', 'v2': 's001','v3': 's005', 'v4': 's005', 'v5': 's009', 'v6': 's007'}
#values = dic.values()
#print(list(values))
#set_values = set(list(values))
#print(set_values)

#2.	Дан словарь {‘name’: ‘Alex’, ‘age’: 12, ‘class’: ‘v’, ‘roll_id’: ‘2’}.
# Проверить принадлежат ли следующие значения  словарю:
# ‘class’, ‘Alex’, ‘Michael’, ‘4’, 2, ‘2’, ‘age’, ‘address’, (‘name’, ‘Alex’), (‘class’, ‘x’).

#dict ={'name': 'Alex','age': 12, 'class': 'v','roll_id': '2'}
#dict_values = dict.values()
#dict_keys = dict.keys()
#dict_items = dict.items()
#x = 'v'
#print(x in dict_values, x in dict_keys, x in dict_items)


#3.	Дано два словаря: {‘Ten’: 10, ‘Twenty’: 20, ‘Thirty’: 30} и
# {‘Thirty’: 30, ‘Fourty’: 40, ‘Fifty’: 50}. Объедините эти словари в один.

#dict1 = {'Ten':10, 'Twenty': 20, 'thirty': 30}
#dict2 = {'Thirsty': 30, 'Fourty': 40, 'Fifty':50}
#dict1.update(dict2)
#print(dict1)

#4.	Дан словарь {‘class’: {‘student’: {‘name’: ‘Mike’, ‘marks’: {‘physics’: 70, ‘history’: 80}}}}.
# Выведите на экран имя студента и его оценку по истории.
#dict ={'class':{'student':{'name': 'Mike','marks': {'physics': 70, 'history': 80}}}}
#dict1 = dict['class']
#dict2 = dict1['student']
#dict3 = dict2['marks']
#print(dict2['name'], dict3['history'])

#5.	Дан словарь {‘gold’: 500, ‘pouch’: [‘flint’, ‘twine’, ‘gemstone’],
# ‘backpack’: [‘xylophone’, ‘dagger’, ‘bedroll’, ‘bread loaf’]}.
# Добавьте в словарь еще один элемент ‘pocket’, содержащий следующие значения: ‘seashell’, ‘strange berry’, ‘lint’.
# Отсортируйте значения, принадлежащие ключу ‘backpack’ и затем удалите из них значение ‘dagger’.
# Увеличьте  на 50 значение, принадлежащее ключу ‘gold’.

dict ={'gold': 500,'pouch':['flint','twine', 'gemstone'],'backpack':['xylophone','dagger','bedroll','bread loaf']}
dict.update({'pocket': ['seashell','strange berry','lint']})
print(dict)
dict3 = dict['backpack']
dict3_sort = sorted(dict3)
print(dict3_sort)
dict3_sort_rem = dict3_sort.remove('dagger')
print(dict3_sort)
value = dict['gold']
print(value * 50)























