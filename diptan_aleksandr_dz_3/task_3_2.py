dict_for_examp = {"zero": "ноль",
                  "one": "один",
                  "two": "два",
                  "three": "три",
                  "four": "четыре",
                  "five": "пять",
                  "six": "шесть",
                  "seven": "семь",
                  "eight": "восемь",
                  "nine": "девять",
                  "ten": "десять"
                  }


def num_translate_adv(number='No such digit'):
    """
    Функция переодит числительные на руский язык. В случае отсутствия цифры в словаре - возвразает None.
    :param number:  Принимает переданное значение и проверяет его наличие в словаре
    :return: Возвращает обработанное значение
    """
    number = number.lower()  # Для корректного сравнения перевожу переменную в нижний регистр.
    your_digit = ''
    your_digit = dict_for_examp.get(number)  # Использую метод get() для получения None если элемент не в словаре
    if your_digit != None:
        your_digit = your_digit.title()  # Применяю метод title() для того, чтобы первая буква была заглавной
    return your_digit


print(f'Digits to check func: {num_translate_adv("two1")} and {num_translate_adv("thrEe")}, {num_translate_adv("nine")}')
