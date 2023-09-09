def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    return chr((ord(letter) - 97 + shift) % 26 + 97)


##2


def caesar_cipher(text: str, shift: int) -> str:
    """Шифр цезаря"""
    res = ''
    for i in text:
        if i.isalpha():
            res += shift_letter(i, shift)
        elif i in [' ', ',', '.', '?', '!']:
            res += i
    return res


####3
# n = int(input())
# arr = [input() for _ in range(n)]


def get_word_indices(arr: list[str]) -> dict:
    """Функция возвращает словарь, где ключи — это уникальные слова из
    списка строк в нижнем регистре, а значения —
    это списки индексов строк, в которых эти слова встречаются"""
    d = {i: 0 for j in arr for i in j.lower().split()}
    for i in d:
        a = []
        for j in range(len(arr)):
            if i in arr[j].lower():
                a.append(j)
        d[i] = a
    return d


###4
def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0, matrix: list = None):
    """Функция  должна возвращать квадратную матрицу , на диагонали которой располагаются числа от 1 до size.
     Все остальные элементы заполнены согласно параметрам up_fill и down_fill"""
    if matrix == None:
        matrix = []

    for i in range(size):
        matrix.append([0] * size)

    for i in range(size):
        cnt = i + 1
        for j in range(size):
            if i == j:
                matrix[i][j] = cnt
            elif i < j:
                matrix[i][j] = up_fill
            else:
                matrix[i][j] = down_fill

    return matrix


def only_one_positive(*args: int):
    count = 0
    for i in args:
        if i >= 0:
            count += 1
    if count == 1:
        print(True)
    else:
        print(False)


def print_goods(*args):
    counter = 1
    for i in args:
        if type(i) == str and len(i) > 0:
            print(f'{counter}. {i}')
            counter += 1

    if counter == 1:
        print("Нет товаров")


def info_kwargs(**kwargs):
    """ данный вызов печатает следующие строки
        age = 33
        first_name = John
        last_name = Doe
    """
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


def create_actor(**kwargs):
    """функцию create_actor, которая принимает произвольное количество именованных аргументов и
       возвращает словарь с характеристиками актера. Если функции create_actor не передавать никаких аргументов,
       то она должна возвращать базовый словарь с ключами name, surname, age
    """
    persons = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }

    return persons | kwargs

# print(create_actor())
# print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))
from pprint import pprint
n, m = [int(i) for i in input().split()]
mat = [[0] * int(m) for i in range(n)]

c = 1
a, b = 0, 0
rows = n - 1
cols = m - 1

while a <= cols and b <= rows:
    for i in range(a, cols + 1):
        mat[a][i] = c
        #c += 1
    b += 1
    for i in range(b, rows + 1):
        mat[i][cols] = c
        #c += 1
    cols -= 1
    if b <= rows:
        for i in range(cols, a-1, -1):
            mat[rows][i] = c
            #c += 1
        rows -= 1
    if a <= cols:
        for i in range(rows, b-1, -1):
            mat[i][a] = c
            #c += 1
        a += 1
        c += 1
A = []
for s in mat:
    A.append(s)
pprint(A)








