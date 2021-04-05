import sys
file_with_prices = 'bakery.csv'


def load_prices(file):
    """ Функция загружает данные из файла
    :param file: Входной файл
    :return: Возвращает список из полученных цен
    """
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()


def show_prices(prices_list):
    """ Функция выводит заданные цены из списка
    :param prices_list: Список с ценами
    :return:
    """
    for price in prices_list:
        print(price)


def get_prices(price_out):
    """ Функция формирует список цен, в зависимости от переданных значений в параметре argv
    :param price_out: Входной список
    :return:
    """
    if len(sys.argv) == 3:
        first_arg = sys.argv[1]
        second_arg = sys.argv[2]
        show_prices(price_out[int(first_arg)-1:int(second_arg)-1])
    elif len(sys.argv) == 2:
        first_arg = sys.argv[1]
        show_prices(price_out[int(first_arg)-1:])
    else:
        show_prices(price_out)


prices = [row.strip() for row in load_prices(file_with_prices)]  # Готовим список

if __name__ == '__main__':
    get_prices(prices)
