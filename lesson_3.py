# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# def my_round(number, ndigits):
#     pass
#
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Решение задания № 1

# def my_round(number, ndigits = False):
#     if ndigits:
#         return float(f"{float(number + (5 / (100 ** ndigits))):.{ndigits}f}")
#     else:
#         return int(number + 0.5)
#
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


# Решение задания № 2

# def lucky_ticket(ticket_number):
#     tn_arr = list(str('{:<06}'.format(ticket_number)))
#
#     sum_value_one = sum(list(map(lambda x: int(x), tn_arr[:3])))
#     sum_value_two = sum(list(map(lambda x: int(x), tn_arr[3:])))
#
#     if sum_value_one == sum_value_two:
#         return "Билет счастливый"
#     else:
#         return "Билет несчастливый"
#
#
# print(lucky_ticket(123006))
# print(lucky_ticket(123210))
# print(lucky_ticket(436751))


# NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


# Решение задания № 1


# def fibonacci(n, m):
#     x = 1
#     y = 1
#     f_list = [1, ]
#
#     for i in range(m):
#         x, y = y, x + y
#         f_list.append(x)
#
#     return f_list[n - 1:m]
#
#
# print(fibonacci(1, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# Решение задания № 2


# def sort_to_max(arr):
#     n = 1
#     while n < len(arr):
#         for i in range(len(arr) - n):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#         n += 1
#     return arr
#
#
# print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# def parallelogram(a1, a2, a3, a4):
#     if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and \
#        abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
#         return True
#     return False