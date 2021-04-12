from functools import wraps


def simple_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        some_string = ''
        # делаю цикл для применения декоратора к каждой передаваемой переменной
        for i in args:
            some_string += f'{func.__name__}({i}: {type(i)}) '
        print(some_string)
        return result
    return wrapper


@simple_logger
def calc_cube(d, *args):  # Функция принимает один именованный аргумент, и второй в виде списка
    return d ** 3, list(map(lambda x: x ** 3, args))  # Далее, возвращаем по очереди, результат работы функции для
# именованного аргумента и затем для списка args, к которому применяю функцию map для итерации списка объектов, а саму
# map оборачиваю в список.


got_cubbed = calc_cube(5, 3, 7, 2)
# print(got_cubbed)
# print(calc_cube.__name__)
