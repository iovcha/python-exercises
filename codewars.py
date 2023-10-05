def find_even_index(arr):
    """Найти индекс равновесия массива"""
    left = [0] * len(arr)
    for i in range(1, len(arr)):
        left[i] = left[i - 1] + arr[i - 1]

    right = 0
    indexs = []
    for i in reversed(range(len(arr))):
        if left[i] == right:
            indexs.append(i)
        right += arr[i]
    return min(indexs) if len(indexs) != 0 else -1

def find_even_index1(arr):
    '''Другое решение  '''
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

def dirReduc(arr):
    """Напишите функцию dirReduc, которая будет принимать массив строк
     и возвращать массив строк с удаленными ненужными направлениями (W<->E или S<->N рядом )."""

    destinace = {"NORTH":"SOUTH","SOUTH":"NORTH", "EAST":"WEST", "WEST":"EAST"}
    for i in range(len(arr) - 1):
        if arr[i + 1] == destinace[arr[i]]:
            del arr[i], arr[i]
            return dirReduc(arr)
    return arr

# num = 70304
# l = []
# for index, digit in enumerate(str(num)[::-1]):
#     if int(digit) != 0:
#         l.append(digit + "0" * index)
# print(' + '.join(l[::-1]))  ###70000 + 300 + 4


def tower_builder(n_floors):
    """Постройте башню в форме пирамиды как массив/список строк, заданный положительным целым числом
      "  *  ",
      " *** ",
      "*****"
      """
    tower = []
    floor = ''
    for i in range(n_floors):
        starts = '*' * (i * 2 + 1)
        l = ' ' * (n_floors - i - 1)
        floor = l + starts +l
        tower.append(floor)
    return tower


#Как проверить, является ли переменная целое число или нет? is_integer()
# n = 114
# num = (n ** 0.5)
# if num.is_integer():
#     print(int(num + 1) ** 2)
# else:
#     print(-1)




def domain_name(url):
    if url.startswith('http://www.'):
        s1 = url.replace('http://www.', '')
        s2 = s1.split('.')
        return s2[0]
    elif url.startswith('http://'):
        s1 = url.replace('http://', '')
        s2 = s1.split('.')
        return s2[0]
    elif url.startswith('www.'):
        s1 = url.replace('www.', '')
        s2 = s1.split('.')
        return s2[0]
    elif url.startswith('https://'):
        s1 = url.replace('https://', '')
        s2 = s1.split('.')
        return s2[0]

    else:
        s1 = url.split('.')
        return s1[0]
#print(domain_name("http://www.codewars.com/kata/"))

# s = "breakCamelCase"
# result = ''
# for letter in s:
#     if letter.isupper():
#         result += f" {letter}"
#     else:
#         result += letter
# print(result)

def sum_dig_pow(a, b):
    arr = []
    for x in range(a, b+1):
        char = []
        n = 0
        for i in str(x):
            char.append(int(i) ** (n + 1))
            n += 1
        if x == sum(char):
            arr.append(x)
    return arr
#print(sum_dig_pow(89,135))


def encrypt_one(s):# Шифрование текста
    a = ''
    b = ''
    for x, y in enumerate(s, 1):
        if x % 2 == 1:
            a += y
        else:
            b += y
    return a + b


def encrypt(s, n): # Шифрование текста n раз
    text = [s]
    for i in range(1, n + 1):
        text.append(encrypt_one(text[i - 1]))
    return text[n]
#print(encrypt(" Tah itse sits!", 3))

# s = "The sunset sets at twelve o' clock."
# s_new = []

# for i in range(97, 123):
#     alphabet.append(chr(i))
# print(alphabet)
# alphabet = [chr(i) for i in range(97, 123)]
# print(alphabet)
#
# for i in s.lower():
#     if i in [' ',',','.','?','!', '-','(',')']:
#         continue
#     if i in alphabet:
#         s_new.append(str(alphabet.index(i) + 1))
# print(' '.join(s_new))


def diamond(n):
    """Вам нужно вернуть строку, которая при печати на экране выглядит
     как ромбовидная форма, используя *символы звездочки"""
    if n < 1 or n % 2 == 0:
        return None
    d = [' ' * ((n - i) // 2) + "*" * i for i in range(1, n , 2)]
    d.extend([' ' * ((n-i)//2) + '*' * i for i in range(n, 0, -2)])
    return '\n'.join(d) + '\n'
print(diamond(5))











































































