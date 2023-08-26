from string import punctuation


def remove_punctuations(word):
    """создаем функцию удаления знаков пунктуации"""
    for punct in punctuation:
        if punct in word:
            word = word.replace(punct, "")
    return word


def longest_word_in_file(file_name: str) -> str:
    """ функцию , которая принимает имя файла и внутри его содержимого находит
       самое длинное слово и возвращает его в качестве ответа. В случае,  если есть несколько слов
       с максимальной длиной, нужно вернуть слово,
       которое встречается последнее в тексте."""
    with open(file_name, encoding='utf-8') as fw:
        max_word = ''
        for i in fw:
            words = i.split()
            for word in words:
                word_whith_punct = remove_punctuations(word)
                if len(word_whith_punct) >= len(max_word):
                    max_word = word_whith_punct
        return max_word


from string import punctuation


def longest_word_in_file2(file_name):
    with open(file_name, encoding='utf-8') as f:
        l = []
        for word in f.read().split():
            word = word.strip(punctuation)
            l.append(word)
        return sorted(l, key=lambda x: len(x))[-1]


####

# with open(r"D:\Downloads\numbers (2).txt", encoding='utf-8') as fw:
#     #print(fw.read())
#     count = []
#     summa = []
#     for num in fw.read().replace(', ', ' ').split():
#         if len(num) == 3:
#             count.append(num)
#         elif len(str(num)) == 2:
#             summa.append(int(num))
#     print(len(count), sum(summa), sep=',')


####
def find_lines_len_more_6(file_name: str) -> int:
    """которая принимает имя файла и находит количество строк, превышающее 6 символов"""
    with open(file_name, 'r', encoding="utf-8") as fw:
        rows = fw.readlines()
        count = 0
        for row in rows:
            if len(row.strip()) > 6:
                count += 1
        return count


####
# with open(r'D:\Downloads\lorem.txt', 'r', encoding='utf-8') as fw:
#     rows = fw.readlines()
#     words = set()
#     for row in rows:
#         for word in row.lower().split():
#             words.add(word)
#     print(len(words))

#####
# with open(r"D:\Downloads\lorem (1).txt", 'r', encoding='utf-8') as fw:
#     words = {}
#     for row in fw.readlines():
#         for word in row.upper().split():
#             words[word] = words.get(word, 0) + 1
#     print(words)

####
# with open(r"D:\Downloads\words.txt", encoding='utf-8') as f:
#     d = []
#     for i in f.readlines():
#         j = i.replace('\n', '').upper()
#         if j[-2:] =='ЕЯ' and  j not in d :
#             d.append(j)
#     print(*sorted(d, key=lambda x: len(x)), sep='\n')


#####
# from string import ascii_lowercase
# import json
#
# v = [i for i in range(1, 27)]
# k = [i for i in ascii_lowercase]
# alphabet = dict(zip(k, v))
# #print(alphabet)
# json_data = json.dumps(alphabet)
# print(json_data)

####
# import json
# maximum = 0
# max_name =''
# max_last_name = ''
# with open(r"D:\Downloads\manager_sales.json") as fw:
#      file = json.load(fw)
#      for elem in file:
#          name = elem['manager']['first_name']
#          last_name = elem['manager']['last_name']
#          total = 0
#          for car in elem['cars']:
#              total += car['price']
#
#          if total > maximum:
#              maximum = total
#              max_name = name
#              max_last_name = last_name
#      print(max_name, max_last_name, maximum)

###
# import json
# maximum = 0
# max_ident = 0
# with open(r"D:\Downloads\group_people.json") as f:
#     data = json.load(f)
#
#     for elem in data:
#         #print(elem)
#         ident = elem['id_group']
#         total = 0
#         for woman in elem['people']:
#             #print(woman)
#             if woman['gender'] == 'Female' and  woman['year'] > 1977:
#                 total += 1
#         if total > maximum:
#             maximum = total
#             max_ident = ident
#     print(max_ident, maximum)

####
# import json
# decoded_text = ''
# with open(r"D:\Downloads\Abracadabra__1_.txt") as fw:
#     text = fw.read()
#     with open(r"D:\Downloads\Alphabet.json") as f:
#          data = json.load(f)
#     for letter in text:
#         if letter in data:
#             decoded_text += data[letter]
#         else:
#             decoded_text += letter
#     with open('decoded_text', 'w') as file:
#         file.write(decoded_text)
#         print(decoded_text)

####
# import json
#
# people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, {"name": "Matthew King", "country": "Colombia", "age": 34}, {"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, {"name": "Sarah Contreras", "country": "Honduras", "age": 82}, {"name": "Danielle Williams", "country": "Togo", "age": 91}, {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, {"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, {"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, {"name": "Christina Fernandez", "country": "Burundi", "age": 71}, {"name": "Allen Norton", "country": "Montserrat", "age": 79}]'
# data = json.loads(people)
# people_sort = sorted(data, key=lambda x: (x['age'], x['name']))
# for i in people_sort:
#     print(f"{i['name']}, {i['country']}, {i['age']}")

####
# import json
#
#
# json_string = '''
# {
#     "customers":[
#         {
#             "userid": 123456,
#             "username": "Allie Hsu",
#             "phone": [
#                 "000-001-0002",
#                 "000-002-0002"
#             ],
#             "is_vip": true
#         },
#         {
#             "userid": 223678,
#             "username": "Donald Duck",
#             "phone": null,
#             "is_vip": false
#         }
#     ]
# }
# '''
#
# data = json.loads(json_string)
# print(data['customers'][0]['username'])

####

# from typing import Generator
#
# def gen_fibonacci_numbers(n: int) -> Generator[int, int,None]:
#     f1, f2 = 1, 1
#     for i in range(n):
#         yield f1
#         f1, f2 = f2, f1 + f2
#
#
# for i in gen_fibonacci_numbers(10):
#    print(i)

####

# def my_range_gen(*args):
#    if len(args) == 1:
#        start = 0
#        stop = args[0]
#        step = 1
#    elif len(args) == 2:
#        start = args[0]
#        stop = args[1]
#        step = 1
#    elif len(args) == 3:
#        start = args[0]
#        stop = args[1]
#        step = args[2]
#    else:
#        raise TypeError('my_range_gen expects 1-3 arguments, got ' + str(len(args)))
#
#    if step == 0:
#        return
#
#    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
#        return
#
#    i = start
#    while (step > 0 and i < stop) or (step < 0 and i > stop):
#        yield i
#        i += step
# for i in my_range_gen(5):
#   print(i)

####
# def from_hex_to_rgb(color: str) -> tuple:
#     """создать функцию которая принимает на вход строку - закодированный код цвета в формате RGB
#      и возвращает кортеж из трех значений (оттенок_красного, оттенок_зеленого, оттенок_синего)"""
#     hex = color.lstrip('#')
#     rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
#     return rgb
#
#
# colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
#           '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
#           '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
#           '#7CFC00', '#7FFF00', '#ADFF2F']
#
# for red, green, blue in map(from_hex_to_rgb, colors):
#     print(f"Red={red}, Green={green}, Blue={blue}")

####
s = input().split()
a = list(map(lambda x: (str(x).upper(), str(x).lower()), s))
print(a)
