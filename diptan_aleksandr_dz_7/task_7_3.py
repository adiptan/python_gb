import os
import shutil


for root, dirs, files in os.walk('.'):
    for file in files:
        relate_path = os.path.relpath(os.path.join(root, file))  # Получаю относительный путь до файла
        if 'template' in relate_path:  # Выбираю только папки, в именах которых есть слово template
            splited_path = os.path.split(relate_path)[0].split('\\')  # Получаю список из элементов пути
            if splited_path[1] != 'templates':  # Выбираю только целевые папки
                new_dir = os.path.join(splited_path[0], splited_path[2], splited_path[1])  # Готовлю целевой путь
                new_file = os.path.basename(relate_path)  # Готовлю имена файлов
                if not os.path.exists(new_dir):  # Если такого пути нет - создаю сразу с вложенными папками
                    os.makedirs(new_dir)
                    print(f'Directory created - {new_dir}')
                else:
                    print(f'Directory exist - {new_dir}. Nothing to create.')
                if not os.path.exists(os.path.join(new_dir, new_file)):  # Проверяю есть ли целевой файл
                    shutil.copy(relate_path, new_dir)
                    print(f'File copied: {relate_path} --> {os.path.join(new_dir, new_file)}')
                else:
                    print(f'File exist - {new_file}. Nothing to create.')
