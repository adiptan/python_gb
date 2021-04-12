import re


def parse_email(address):
    """ Функция принимает email и проверяет его на валидность.
    :param address:
    :return: словарь, где ключи имя пользователя и домен.
    """
    keys_for_dict = ['username', 'domain']
    parse_result = re.split('@', address)  # использую @ как разделитель имени и домена. Получаю список
    symbols_in_address = re.findall(r'[@/.]', address)  # Ищу в email символы "." и "@". Если адрес
    # валидный - возвращает список из 2 элементов.

    try:
        if len(symbols_in_address) == 2:  # Проверяю, если в списке 2 элемента "." и "@", то всё ок, иначе except
            final_dict = dict(zip(keys_for_dict, parse_result))  # Формирую из 2 списков словарь с помощью zip.
            return final_dict
        else:
            raise ValueError()
    except ValueError:
        print(f'ValueError: wrong email: {address}')


if __name__ == '__main__':
    print(parse_email('someuser@mail.ru'))
