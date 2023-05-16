###1
# def create_accumulator():
#     summa = 0
#     def summator(a):
#         nonlocal summa
#         summa += a
#         return summa
#     return summator
# summator_1 = create_accumulator()
# print(summator_1(1))
# print(summator_1(5))
# print(summator_1(2))
#
# summator_2 = create_accumulator()
# print(summator_2(3))
# print(summator_2(10))

####2
# def create_accumulator(summa=0):
#     def summator(a):
#         nonlocal summa
#         summa += a
#         return summa
#
#     return summator
#
#
# summator_1 = create_accumulator(100)
# print(summator_1(1))  # печатает 101
# print(summator_1(5))  # печатает 106
# print(summator_1(2))  # печатает 108
#
# summator_2 = create_accumulator()
# print(summator_2(3)) # печатает 3
# print(summator_2(4)) # печатает 7

##3
# def multiply(a):
#     def multiplication (b):
#         return a * b
#     return multiplication
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
#
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45

###4


def create_dict():
    count = 0
    a = {}
    def inner(b):
        nonlocal count
        nonlocal a
        count += 1
        a[count] = b
        return a
    return inner

f_1 = create_dict()
print(f_1('hello')) # f_1 возвращает {1: 'hello'}
print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict() # создаем новое замыкание в f_2
print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}
