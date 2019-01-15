# EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


# Решаем Задачу №1:

# Скрипт 1

# import os
#
# for num in range(1, 10):
#     dir_path = os.path.join(os.getcwd(), f'dir_{num}')
#     try:
#         os.mkdir(dir_path)
#     except FileExistsError:
#         print('Такая директория уже существует')

# Скрипт 2

# import os
#
# for num in range(1, 10):
#     dir_path = os.path.join(os.getcwd(), f'dir_{num}')
#
#     if os.path.exists(dir_path):
#         try:
#             os.removedirs(dir_path)
#         except FileExistsError:
#             print('Удаление директории не получилось')
#     else:
#         print('Такой директории не существует')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# import os
#
# list = os.listdir()
# for dir_path in list:
#     if os.path.isdir(dir_path):
#         print(dir_path)