from requests import get
import xml.etree.ElementTree as ET
import datetime as dt

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def get_page_data(url):
    """
    :param url: принимает на вход URL
    :return: возвращает содержимое страницы
    """
    response = get(url)
    content = response.content.decode(encoding='windows-1251')
    return content


def currency_rates(curr='USD'):
    """
    :param curr: код валюты, например USD
    :return: в случае если валюта найдена, возвращается курс валюты и дата полученная с сервера
    """
    list_for_ret = {}
    curr = curr.upper()  # перевожу входную переменную в верхний регистр
    str_to_date = dt.datetime.strptime(root.attrib['Date'], '%d.%m.%Y').date()  # перевожу дату из str в date
    list_for_ret['date'] = str_to_date

    for currencies in root:
        if curr == currencies[1].text:
            list_for_ret['curr'] = currencies[4].text
            return list_for_ret

    return list_for_ret


root = ET.fromstring(get_page_data(URL))  # Убрал из тела функции, чтобы при вызове не запрашивать xml с сервера

print(f'Date of currency - {currency_rates()["date"]}. Rate for USD is {currency_rates("Usd").get("curr")}')
print(f'Date of currency - {currency_rates()["date"]}. Rate for EUR is {currency_rates("EuR").get("curr")}')
print(f'Date of currency - {currency_rates()["date"]}. Rate for TUG is {currency_rates("TUG").get("curr")}')
