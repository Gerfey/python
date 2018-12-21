# Easy
#
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
#
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
#
# Подсказка: воспользоваться методом .format()

# Решение задачи № 1

arr = ["яблоко", "банан", "киви", "арбуз"];

i = 1
for fruit in arr:
    print(f"{i}. {fruit:>6}")
    i += 1

#
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
#

# Решение задачи № 2

one_list = ['м', 'а', 'г', 'и', 'я', ' ', 'у', 'ж', 'е', ' ', 'ч', 'а', 'с', 'т', 'ь', ' ', 'н', 'а', 'с']
two_list = ['у', 'ж', 'е', ' ']

for bold in two_list:
    one_list.remove(bold)

print(one_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Решение задачи № 3

list_count = [3, 2, 5, 8, 12, 43, 76, 23, 89, 89, 65, 34]
new_list = list()

for value_count in list_count:
    if (value_count % 2 == 0):
        new_list.append(value_count / 4)
    else:
        new_list.append(value_count * 2)

print(new_list)

# Normal
#
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]
#

# Решение задачи № 1

def is_instance(n):
    if isinstance(n, (float, int)) and n % 1 == 0:
        return True
    return False


arr_list = [2, -5, 8, 9, -25, 25, 4]
new_list = list()

for value in arr_list:
    if is_instance(value ** 0.5):
        new_list.append(int(value ** 0.5))

print(new_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# Решение задачи № 2

import math


def parser_date(string):
    arr_day = {"1": "первое", "2": "второе", "3": "третье", "4": "четвертое", "5": "пятое", "6": "шестое",
               "7": "седьмое", "8": "восьмое", "9": "девятое", "10": "десятое", "11": "одиннадцатое",
               "12": "двенадцатое", "13": "тринадцатое", "14": "четырнадцатое", "15": "пятнадцатое",
               "16": "шестнадцатое", "17": "семнадцатое", "18": "восемнадцатое", "19": "девятнадцатое",
               "20": {0: "двадцатое", 1: "двадцать"}, "30": {0: "тридцатое", 1: "тридцать"}}

    arr_month = {
        "1": "января", "2": "февраля", "3": "марта", "4": "апреля", "5": "мая", "6": "июня",
        "7": "июля", "8": "августа", "9": "сентября", "10": "октября", "11": "ноября", "12": "декабря"
    }

    date_split_array = string.split('.')

    first_part_of_date = str(math.floor(int(date_split_array[0]) / 10) * 10)
    second_part_of_date = str(int(date_split_array[0]) - math.floor(int(date_split_array[0]) / 10) * 10)

    if (int(date_split_array[0]) < 10 or int(date_split_array[0]) >= 20):
        if first_part_of_date == '0':
            return arr_day[second_part_of_date] + " " + arr_month[date_split_array[1]] + " " + date_split_array[
                2] + " года"
        elif second_part_of_date == '0':
            return arr_day[first_part_of_date][0] + " " + arr_month[date_split_array[1]] + " " + date_split_array[
                2] + " года"
        else:
            return arr_day[first_part_of_date][1] + " " + arr_day[second_part_of_date] + " " + arr_month[
                date_split_array[1]] + " " + date_split_array[2] + " года"
    else:
        return arr_day[date_split_array[0]] + " " + arr_month[date_split_array[1]] + " " + date_split_array[2] + " года"


print(parser_date("20.12.2018"))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

# Решение задачи № 3

import random

n = 100
list_arr = list()

i = 1
while i < n:
    list_arr.append(random.randint(-100, 100))
    i += 1

# Hard
#
# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?

# Решение задачи № 1

nonsense_text = input("Введите текст: ")

words = 0
letters = 0

pos = True
for letter in nonsense_text:

    # Проверяем, сколько английских букв в тексте
    if letter in tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        letters += 1

    # Проверяем, сколько слов в тексте
    if letter != ' ' and pos:
        words += 1
        pos = False
    elif letter == ' ':
        pos = True

print(f"Слов в тексте: {words}")
print(f"Букв английского алфавита в тексте: {letters}")

# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра

# Решение задачи № 2

text_1 = input("Введите первый текст: ")
text_2 = input("Введите второй текст: ")

words_1 = text_1.lower().split(" ")
words_2 = text_2.lower().split(" ")

result = list(set(words_1) & set(words_2))

print(f"В обоих текстах присутсвуют слова: {result}")


# EXTRA
# Есть два словаря. Один это рецепт блюда, второй это список продуктов, которые есть в ходильнике.
#
# Ключ это название продукта, значение - это количество.
#
# Нужно сравнить два словаря и дать словарь, в котором будет список покупок
# Если для рецепта всё есть, то сказать что ничего не нужно
# Разницей по измерению гр, мл, шт. Пренебречь

# Решение задачи EXTRA

shopping_list = {}

# Рецепт Оливье по-советски
recipe = {"Картофель": 7, "Морковь": 5, "Маринованные огурцы": 6, "Консервированный зеленый горошек": 1,
          "Яйцо куриное": 6, "Докторская колбаса": 300, "Сметана": 100, "Майонез": 200, "Соль": 10}

# Что имеем в холодильнике
fridge = {"Картофель": 2, "Морковь": 1, "Яйцо куриное": 2, "Майонез": 50, "Соль": 10}

there_is = list(set(recipe) & set(fridge)) # Получаем список того, что имеем
need_to = list(set(recipe) - set(fridge)) # Получаем список того, чего нет в холодильнике

if len(need_to) > 0:
    for there_is_value in there_is:
        count_there_is = recipe[there_is_value] - fridge[there_is_value]
        if recipe[there_is_value] - fridge[there_is_value] != 0:
            shopping_list[there_is_value] = count_there_is
    for need_to_value in need_to:
        count_need_to = recipe[need_to_value]
        shopping_list[need_to_value] = count_need_to
else:
    print("Для приготовления блюда, ничего не нужно покупать")

print(shopping_list)