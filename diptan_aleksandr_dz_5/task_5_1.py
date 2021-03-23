def gen_digit(dig_count=10):
    """
    :param dig_count: Принимает число как верхнюю границу генератора
    :return: Возвращает генератор
    """
    for i in range(1, dig_count+1):
        if i % 2 != 0:
            yield i


odd_to_15 = gen_digit()
try:  # Добавил обработку исключений
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))

    print(sum(odd_to_15))

    print(next(odd_to_15))
except StopIteration:
    print('Error found: StopIteration')
