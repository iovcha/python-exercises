#Пекарня продает хлеб по $3,49 за буханку. Скидка на вчерашний хлеб составляет 60 %.
# Напишите программу, которая будет запрашивать у пользователя количество приобретенных вчерашних буханок хлеба.
# В вывод на
#экран должны быть включены обычная цена за буханку, цена со скидкой
#и общая стоимость приобретенного хлеба. Все значения должны быть выведены на отдельных строках с
# соответствующими описаниями. Используйте для вывода формат с двумя знаками

cena = 3.49
discount = 0.6
count = int(input('количество приобретенных вчерашних буханок хлеба: '))
print('обычная цена за буханку: %5.2f.' % (cena * count ))
print('скидкa: %5.2f.' % ((cena * count) * discount))
print('общая стоимость приобретенного хлеба: %5.2f.' % ((count * cena) - (cena * count * discount)))