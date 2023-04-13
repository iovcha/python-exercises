# Решения задачи с сохранением ключей
# n = int(input())
#
# database = {}
# for i in range(n):
#     login = input()
#     if login in database:
#         database[login] += 1
#         database[f"{login}{database[login]}"] = 0
#         print(f"{login}{database[login]}")
#     else:
#         database[login] = 0
#         print(f'OK')
# print(database)
from typing import Dict, Any

## 2 Методы словаря
# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
#
# city = input()
# for key, values in countries.items():
#     if city in values:
#         print(f'INFO: {city} is a city in {key}')
#         break
# else:
#     print(f'ERROR: Country for {city} not found')

# ###3
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
#     "date_of_birth": "1993-08-17"
#}
# user["secret"] = user.pop('password')
# user["surname"] = user.pop("last_name")

##4Напишите код для преобразования списка из целых чисел произвольной длины в словарь, вложенность которого зависит от длины списка.
lst = list(map(int, input().split()))
l = len(lst) - 1
dict_lst = {}
while l != 0:
    if len(dict_lst) == 0:
        dict_lst ={lst[l - 1] : lst[l]}
    else:
        dict_lst = {lst[l - 1] : dict_lst}

    l -= 1

print(dict_lst)










