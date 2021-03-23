from requests import get
import xml.etree.ElementTree as ET

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


print(f'Rate for USD is {currency_rates("Usd")}')
print(f'Rate for EUR is {currency_rates("EuR")}')
print(f'Rate for TUG is {currency_rates("TUG")}')
