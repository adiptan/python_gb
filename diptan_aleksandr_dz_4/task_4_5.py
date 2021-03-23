from requests import get
import xml.etree.ElementTree as ET
import sys

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def get_page_data(url):
    """
    :param url: принимает на вход URL
    :return: возвращает содержимое страницы
    """
    response = get(url)
    content = response.content.decode(encoding='windows-1251')
    return content


def currency_rates(curr):
    """
    :param curr: код валюты, например USD
    :return: в случае если валюта найдена, возвращается курс валюты
    """
    curr = curr.upper()  # перевожу входную переменную в верхний регистр
    root = ET.fromstring(get_page_data(URL))

    for currencies in root:
        if curr == currencies[1].text:
            return currencies[4].text
    return


try:
    print(f'Rate for USD is {currency_rates(sys.argv[1])}')
except IndexError:
    print('Please run script from console with params. Example: python task_4_5.py usd')
