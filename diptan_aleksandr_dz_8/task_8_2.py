import re
from time import perf_counter


def timer(func):  # Декоратор для подсчёта времени работы функции
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        start = perf_counter()
        finish = perf_counter()
        print(f'Work time - {finish - start}')
        return result
    return wrapper


@timer
def parse_file():
    new_buffer = []
    file_count_of_string = 0
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        for raw in f:
            file_count_of_string += 1
            raw = raw.strip()
            ip_address = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w+\:\w+\:\w+\:\w+\:\w+\:\w+\:\w+:\w+|\w+\:'
                                 r'\w+\::\w+\:\w+:\w+:\w+|\w+\:\w+\:\w+\:\w+\::\w+)')
            event_date = re.compile(r'\d{2}\/[A-Za-z]\w+\/\d{4}\:\d{2}\:\d{2}\:\d{2}\s\+\d{4}')
            request_type = re.compile(r'[A-Z][A-Z][A-Z]\s')
            requested_app = re.compile(r'\/[a-z]\w+\/[a-z]\w+')
            server_response = re.compile(r'\s\d{3}\s')
            some_last_symbol = re.compile(r'\s(?:\d|\d{1,8})\s+\"')
            try:
                got_parsed_line = ip_address.findall(raw)[0], event_date.findall(raw)[0], request_type.findall(raw)[0],\
                    requested_app.findall(raw)[0], server_response.findall(raw)[0],\
                    some_last_symbol.findall(raw)[0].strip().replace('"', '')
                new_buffer.append(got_parsed_line)
                print(got_parsed_line)
            except IndexError:
                print(f'This is an IndexError, the line not parsed - {raw}')
    print('\n*******************************************************************')
    print(f'Count of string in file: {file_count_of_string} \nCount parsed string: {len(new_buffer)}')
    print('*******************************************************************')


parse_file()
