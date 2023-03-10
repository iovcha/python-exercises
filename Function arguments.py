#name = "Iryna"
#password = "2345jyrSD"

#def check(name, password, attempt=3):
#    attempt = 3
 #   while attempt != 0:
#        login = input("Login: ")
#        pasw = input("Password: ")
#        if login == name and pasw == password:
#            return "Добро пожаловать"
#        if login != name and pasw != password:
#            attempt -= 1
#            print("Ошибка, введите ещё")

#        if attempt == 0:
#             return "Система заблокирована. Повторите попытку через 5 мин."

#print(check(name, password))


#2
#def inform_author( sep=".", **kwargs):
#    n = kwargs['name'][0]
#    p = kwargs['patr'][0]
#    surname = kwargs['surname']
 #   birth = kwargs['birth']
#    death = kwargs['death']
#    krt = kwargs['krt']
#    return f'{n}{sep}{p}{sep}{surname} ({birth} - {death}) - {krt}'

#print(inform_author(name = 'Александр', patr="Сергеевич", surname="Пушкин", birth="6.06.1799 ", death="10.02.1837",
#                    krt="русский поэт, драматург и прозаик."))
#print(inform_author(name='Иван', patr=' ', surname="Соболь",  birth="24.08.1939", death=" ", krt="израильский драматург, писатель и режиссер." ))

#3
def count_rank_number(num):
    count = 1
    num //= 10
    while num > 0:
        num //= 10
        count += 1
    return count

def num_list(*args):
    t = 0
    k = 0
    for num in args:
        if count_rank_number(num) == 2:
            t += 1
        if count_rank_number(num) == 3:
            k += 1
    if t > 0:
        print("Двухзначных чисел: ", t)
    if k > 0:
        print("Трехзначных чисел:", k)
    if t == 0 and k == 0:
         print("Двухзначных и трехзначных  чисел нет")

num_list(7,89, 567, 897, 456,23,876)
num_list(3, 8, 4567)
num_list(6, 78, 78, 56, 98, 45)
num_list(678)











