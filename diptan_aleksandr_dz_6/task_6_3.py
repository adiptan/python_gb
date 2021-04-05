import json


def get_content(file):
    """
    :param file: Принимает на вход имя файла, из которого производится чтение
    :return: Возвращает список
    """
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()


def save_data_to_json(some_data, file='saved_data.json'):
    """
    :param some_data: На вход принимает словарь
    :param file: и имя файла, в который будет записана информация
    :return: ничего не возвращает
    """
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(some_data, f)


def load_data_from_json(file='saved_data.json'):
    """
    :param file: Принимает на вход имя файла, из которого будет загружена информация.
    :return: Возвращает содержимое файла в виде списка
    """
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


users = [user.strip().replace(',', ' ') for user in get_content('users.csv')]  # подготовка списка
hobbies = [hobby.strip() for hobby in get_content('hobby.csv')]
final_dict = {}

for i in range(len(users)):
    if len(users) > len(hobbies):
        hobbies.append(None)
    elif len(users) < len(hobbies):
        print("Exit with code 1")
        raise SystemExit(1)
    final_dict[users[i]] = hobbies[i]

save_data_to_json(final_dict)
print(load_data_from_json())
