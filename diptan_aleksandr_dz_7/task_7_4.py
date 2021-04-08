import os
import collections
import random

folder = 'data'
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]


def generate_files():
    """  Функция при вызове генерирует файлы
    :return: Ничего не возвращает
    """
    for _ in range(10 ** 2):  # Создаю 100 файлов.
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))  # Имя файла от 5 до 10 символов
        f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 4)))  # Размер файла до 10 Кб
        with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:  # Создается файл
            f.write(f_content)  # и в него записывается содержимое


files_dict = collections.defaultdict(list)

if not os.path.exists(folder):  # Создаю папку если такой нет
    os.mkdir(folder)
    some_files_list = os.listdir(folder)
    if len(some_files_list) == 0:  # Если папка пустая, запускаю функцию генерации файлов.
        generate_files()
some_files_list = os.listdir(folder)

for id, item in enumerate(some_files_list):  # Прохожусь по файлам и раскладываю согласно размеров
    file_size = os.stat(os.path.join(folder, item)).st_size
    if file_size <= 100:
        files_dict[100].append(item)
    elif file_size <= 1000:
        files_dict[1000].append(item)
    elif file_size <= 10000:
        files_dict[10000].append(item)

for key, item in sorted(files_dict.items()):
    print(f'{key} {len(item)}')
