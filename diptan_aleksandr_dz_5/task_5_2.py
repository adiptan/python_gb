from itertools import islice


def gen_digit(dig_count=10):
    """
    :param dig_count: Принимает число как верхнюю границу генератора
    :return: Возвращает генератор через islice
    """
    nums_gen = (i for i in range(1, dig_count+1) if i % 2 != 0)
    return islice(nums_gen, dig_count)


dig_count_15 = gen_digit(11)
try:  # Добавил обработку исключений
    print(next(dig_count_15))
    print(next(dig_count_15))
    print(next(dig_count_15))
    print(next(dig_count_15))

    print(sum(dig_count_15))
    print(sum(dig_count_15))

    print(next(dig_count_15))
except StopIteration:
    print('Error found: StopIteration')
