import sys
file_to_write = 'bakery.csv'


def add_data_to_file(data, file=file_to_write):
    """  Функция для записи данных в файл
    :param data: принимает данные для записи в файл и имя файла
    :return:
    """
    if data:
        with open(file, 'a', encoding='utf-8') as f:
            f.write(data+'\n')


def clear_file(file=file_to_write):
    """    Функция для удления всех данных из файла
    :param file: Файл который будет очищен
    :return:
    """
    with open(file, 'w', encoding='utf-8') as f:
        f.write('')


try:
    if sys.argv[1] == 'clear':  # Для очистки файла используется команда clear
        clear_file()
    else:
        add_data_to_file(sys.argv[1])
except IndexError:
    print('Please enter data')
