# ##1.	Определите класс “Прямая” со свойствами:  координаты двух точек (x1, y1) и (x2, y2),
# # - и методами: вывод уравнения прямой и  определение точек пересечения с осями координат.
# class Straightline():
#     """класс “Прямая”"""
#
#     def __init__(self, x1, x2, y1, y2):
#         """координаты двух точек"""
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def equation_straight_line(self):
#         """уравнения прямой"""
#         x_diff = self.x1 - self.x2
#         y_diff = self.y1 - self.y2
#         if x_diff != 0:
#             k = y_diff / x_diff
#             b = self.y2 - k * self.x2
#             if b > 0:
#                 print(f'y = {k} * x + {b}')
#             else:
#                 print(f'y = {k} * x - {abs(b)}')
#         else:
#             print("Уравнение прямой, проходящей через эти точки:")
#             print(f'x = {self.x1}')
#
#     def determination_point(self):
#         """определение точек пересечения с осями координат"""
#         x_diff = self.x1 - self.x2
#         y_diff = self.y1 - self.y2
#         if x_diff != 0:
#             k = y_diff / x_diff
#             b = self.y2 - k * self.x2
#             print(f"Точка пересечения с ОУ ({b}, 0)")
#             print(f"Точка пересечения с OX (0, {-b / k})")
#
#
# line1 = Straightline(1, 3, 2, 7)
# line2 = Straightline(4, 0, 0, 5)
# line1.equation_straight_line()
# line2.equation_straight_line()
# line1.determination_point()
# line2.determination_point()

####2
# class BlogPost:
#     def __init__(self, user_name, text,  number_of_likes):
#         self.user_name = user_name
#         self.number_of_likes = number_of_likes
#         self.text = text
#
# instagram1 = BlogPost(user_name="Annna",text="i like my life", number_of_likes=245)
# print(instagram1.number_of_likes)
# instagram2 = BlogPost(user_name="Elena",text='I like a road trip', number_of_likes=6000)
# print(instagram2.number_of_likes)

####3
# class BankAccount:
#
#     def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
#         self.client_id = client_id
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         self.balance = balance
#
#     def add(self, s):
#         """можно пополнять счет"""
#         self.balance += s
#
#
#     def withdraw(self, s):
#         """выводить средства со счета"""
#         self.balance -= s
#
# client_1 = BankAccount("FJ 2580", 'Adam', 'Black', 2000.0)
# client_2 = BankAccount("FH 7100", 'Mateo', 'White', 7000.0)
# client_1.add(1000)
# print(client_2.balance)
# client_1.withdraw(500)
# print(client_1.balance)


# #####4
# class GameCharacter:
#
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#
#     def speak(self):
#         print(f'Hi, my name is {self.name}')
#
#
# class Villain(GameCharacter):
#     def __init__(self,name, health, level):
#         GameCharacter.__init__(self,name, health, level)
#
#     def speak(self):
#         print(f'Hi, my name is {self.name} and I will kill you')
#
#     def kill(self):
#         self.health = 0
#         print('Bang-bang, now your\'e dead')
#
# adam = Villain("Adam", 4, 7)
# met = GameCharacter('Met', 8, 8)
# met.speak()
# adam.speak()
# adam.kill()
# print(adam.health)
# print(met.health)

###5
# class Soda:
#
#     def __init__(self, additive=None):
#         if isinstance(additive, str):
#             self.additive = additive
#         else:
#             self.additive = None
#
#     def show_my_drink(self):
#         if self.additive:
#             print(f'Газировка и {self.additive}')
#         else:
#             print(f'Обычная газировка.')
#
#
# drink_1 = Soda('limon')
# drink_2 = Soda()
# drink_1.show_my_drink()
# drink_2.show_my_drink()


###6
class TriangleChecker:

    def __init__(self, a, b, c):
        self. sides = [a, b, c]

    def is_triangle(self):
        ''' требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.'''
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'

figure_1 = TriangleChecker(4, 6, 8)
figure_2 = TriangleChecker(2, 'ask', 10)
figure_3 = TriangleChecker(-9, 7, -2)
figure_4 = TriangleChecker(12, 2, 1)
print(figure_1.is_triangle())
print(figure_2.is_triangle())
print(figure_3.is_triangle())
print(figure_4.is_triangle())


