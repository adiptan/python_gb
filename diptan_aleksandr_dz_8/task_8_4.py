from functools import wraps


def decor(some_arg):
    print(type(some_arg))  # в качестве артгумента, передаю в декоратор lambda-функцию
    print(some_arg)

    def _decor(func):
        @wraps(func)  # маскирование работы декоратора
        def wrapper(*args, **kwargs):
            msg = f'Wrong val {args}'
            if not some_arg(*args, **kwargs):  # Передаю lambda-функции аргументы из основной функции.
                raise ValueError(msg)  # Error если вернётся False
            else:
                result = func(*args, **kwargs) # Если True - возвращаю результат работы основной функции.
                print('********************************************')
                print(f'Result of function is {result}')
                print('********************************************')
            return result
        return wrapper
    return _decor


@decor(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


# на всякий случай, обернул в try...except, чтобы не выглядело как ошибка :)
try:
    a = calc_cube(3)
except ValueError:
    print('ValueError')

print(calc_cube.__name__)
