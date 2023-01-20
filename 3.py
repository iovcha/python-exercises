#string = 'Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$.'
#byte_string = string.encode()
#print(byte_string)
#byte_string_arr = bytearray(byte_string)
#print(byte_string_arr)
#del byte_string_arr[2::3]
#print(byte_string_arr.decode())

#sms= b'\xe6\x88\x81\xa3@\x89\xa2@\xa8\x96\xa4\x99@\x86\x81\xa5\x96\xa4\x99\x89\xa3\x85@' \
 #   b'\x97\x99\x96\x87\x99\x81\x94\x94\x89\x95\x87@\x93\x81\x95\x87\xa4\x81\x87\x85o'
#sms_encode = sms.decode(encoding='cp037')
#print(sms_encode)
#answer = 'Python'
#answer_encode = answer.encode(encoding='cp037')
#print(answer_encode)

#text ='All the world’s a stage, and all the men and women merely players. They have their exits and their entrances;\
 #         and one man in his time plays many parts.'
#t_lower = text.lower()
#text_set = set(t_lower)
#print(text_set)
#print(len(text_set))
#print(min(text_set),'elemens')
#print(max(text_set), 'elemens')

#fizika = ['Максим', 'Матвей', 'Александр']
#matem = ['Матвей', 'Евгения', 'Михаил', 'Максим', 'Наталья']
#general_list = set(fizika) | set(matem)
#print('Общий список по двум дисциплинам: ', str((list(general_list))).strip('[]'))
#award_winners = set(fizika).intersection(set(matem))
#print('Ребята, занявшие призовые места по двум дисциплинам: ', str(list(award_winners)).strip('[]'))
#not_winners = set(matem).difference(set(fizika))
#print('ребятa, которые не вошли в тройку призеров в олимпиаде по физике:  ', str(list(not_winners)).strip('[]'))
#del fizika

import math
product = {'smart watch': 550, 'phone': 1000, 'playstation': 500, 'laptop': 1550, 'music player': 600, 'tablet': 400}
print('Общая стоимость:' ,sum(product.values()))
product_name = product.keys()
print(product_name)
print('В алфавитном попядке:', sorted(product_name, key=None))
print('В обратном пррядке:', sorted(product_name, key=None,reverse=True))
product['music player'] = int( product['music player'] * 0.5)
print(product)
sum = 5 * product['phone'] + product['laptop'] * 3
tablet_count = math.ceil((sum / product['tablet']))
print(tablet_count)
prize = product.popitem()
print('priz:', prize[0])
print(product)
product.update({'iphone': 1300, 'music player': 850, 'headphones':  200})
print(product)




