# 1.	Определите, сколько раз в тексте встречается заданное слово
# (взять произвольный текст и проверить решение для 2-3 разных слов).

#t = b'First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus.' \
 #   b' I like to go to school. It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple.'
#count_i = t.count(b'I')
#count_do = t. count(b'do')
#count_not =t.count(b'not')
#print(count_i, count_do, count_not)

#2.	Дана строка. Проверить, сколько слов заканчивается на букву “e”.
#t = b' Agree  Agreeable  Definite  Definitely'
#count_e = t.count(b'e ')
#print(count_e)

#4.	Дана строка, состоящая из одного слова. Преобразуйте строку таким образом,
# чтобы все буквы были разделены между собой пробелами.

#string = 'First'
#s =' '
#string_s =s.join(string).encode()
#print(string_s)

#2.	Дана байтовая строка. Перевести ее в шестнадцатеричный формат. Проверить результат по таблице ASCII.
#string = b'I wake up.'.hex()
#print(string)

#3.	Необходимо декодировать закодированную с помощью кодировки  cp866 строку:

#b'\x8c\xae\xab\xae\xa4\xa5\xe6!\x8e\xe2\xab\xa8\xe7\xad\xa0\xef \xe0\xa0\xa1\xae\xe2\xa0!'
#Декодируйте ту же самую строку с помощью кодировки ascii.  В случае возникновения ошибки, проигнорируйте ее программным способом.





string = b'\x8c\xae\xab\xae\xa4\xa5\xe6!\x8e\xe2\xab\xa8\xe7\xad\xa0\xef \xe0\xa0\xa1\xae\xe2\xa0!'
try:
    string_d = string.decode('cp866')
    string = string.decode('ascii')
except UnicodeDecodeError: 'ascii'
print(string_d)













