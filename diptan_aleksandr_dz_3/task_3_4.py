def thesaurus(*args, need_sort=False):
    """
    :param args: Всё что подаётся на вход распаковываем в список
    :param need_sort: Флаг. Если нужна сортировка - True, иначе - False
    :return: Функция возвращает словарь где ключ первая буква фамилии, внутри ещё один словарь,
    ключи которого первые буквы имени, а элемент это список переданных в функцию имен.
    """
    dict_main = {}
    for el in args:
        surname = el.split()[1]
        name = el.split()[0]
        val_list = [el]
        first_letter_surname = surname[0]  # Присваиваю переменной значение первой буквы имени
        first_letter_name = name[0]
        if first_letter_surname not in dict_main:
            dict_main[first_letter_surname] = {first_letter_name: val_list}
        else:
            dict_main[first_letter_surname].setdefault(first_letter_name, [])  # Создаю внутри словарь, значение -список
            dict_main[first_letter_surname][first_letter_name].append(el)  # Добавляю имя в список

# Сортировка сделана с помощью флага
    if need_sort:  # Если флаг need_sort = True
        keys_list = [key for key in dict_main.keys()]  # Создаю список ключей словаря
        keys_list.sort()  # Сортирую элементы списка
        changed_dict = {}
        for i in keys_list:  # И добавляю отсортированные элементы в качестве ключей в новый словарь, а в качестве
            changed_dict[i] = dict_main[i]  # значений беру элементы в исходном словаре.
    else:
        return dict_main  # Иначе, возвращаю исходный словарь dict_main

    return changed_dict  # Иначе возвращаю созданный словарь changed_dict


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                "Илья Иванов", "Анна Савельева", "Эдуард Сатьянов",
                "Владимир Нисвелидзе", "Артём Карпенков", need_sort=True))
