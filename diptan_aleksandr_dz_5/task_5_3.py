tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def klass_func():
    """
    :return:  Функция возвращает генератор содержащий кортежи вида tutor, klass
    """
    if len(tutors) < len(klasses):  # Проверяю, если в длинна списка tutors < klasses - добавляю значение None в список
        tutors.append(None)
    for tutor, klass in zip(tutors, klasses):  # Склеиваю значение списков через функцию zip
        klass_tutor_tuple = tutor, klass  # На выходе получаю кортежи
        yield klass_tutor_tuple


people_in = klass_func()
try:  # Добавил обработку исключений
    print(type(people_in))  # Проверяю тип полученной переменной
    print(next(people_in))
    print(next(people_in))
    print(next(people_in))
    print(next(people_in))
    print(next(people_in))
    print(next(people_in))
    print(next(people_in))
    print(next(people_in))
    print(next(people_in))
except StopIteration:
    print('Error found: StopIteration')
