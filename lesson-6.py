# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления (не печати, нужен return) площади, периметра  и вывод значений сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)


# Решение задания №1


# class Triangle:
#
#     def __init__(self, a: float, b: float, c: float):
#         self.a = a
#         self.b = b
#         self.c = c
#
#         if (a == 0 or b == 0 or c == 0):
#             print("Такой треугольник нельзя создать")
#             exit(1)
#
#     def square(self):
#         return (self.a + self.b + self.c) * 0.5
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def getSides(self):
#         return f"a: {self.a} b: {self.b} c: {self.c}"
#
#
# triangle = Triangle(10, 5, 7.5)
#
# print(f"Площадь: {triangle.square()}")
# print(f"Периметр: {triangle.perimeter()}")
# print(f"Стороны треугольника: {triangle.getSides()}"

