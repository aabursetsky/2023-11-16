import os
import time

directory = "."

for root, dirs, files in os.walk(directory):  # (root, dirs, files)
    for file in files:
        filepath = os.path.join(root, file)  # полный путь
        filetime = os.path.getmtime(filepath)  # время последней модификации файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # день.месяц.год часы:минуты
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)  # родитеьский каталог

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        print('Родительская директория: ', os.path.abspath(os.path.join(filepath, os.pardir)))  # Полный путь
