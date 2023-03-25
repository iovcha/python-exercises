count= int(input())
result =""
for _ in range(count):
    s = input()  # получаем строку рецепта
    if 'соль' in s:  # если есть слово  соль то пропускаем эту строку
        continue
    result += s + ', '  # собираем результат
print(result[:-2])
