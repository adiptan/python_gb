# Сделал сразу с одним списком, чтобы, также, выполнить и ДЗ №3 :).
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

part = 0

while part < len(start_list):
    some_var = start_list[part]
    if some_var.isdigit():
        del start_list[part]  # Удаляю исходный элемент списка
        start_list.insert(part, '"')  # Добавляю кавычку
        part += 1  # Делаю смещение на один элемент вправо по списку
        start_list.insert(part, f'{int(some_var):02}')   # Затем, добавляю число с помощью insert
        part += 1  # Делаю ещё одно смещение
        start_list.insert(part, '"')  # Добавляю ещё одну кавычку
        part += 1  # Делаю финальное смещение для этого условия и.т.д
    elif some_var[0] in '+-':
        del start_list[part]
        start_list.insert(part, '"')
        part += 1
        start_list.insert(part, some_var[0] + '0' + some_var[1:])
        # # Если в нулевом элементе, элемента списка есть знаки (+-), то формирую строку из этого знака + 0 + число
        part += 1
        start_list.insert(part, '"')
        part += 1
    part += 1

final_sting = ''  # Объявил переменную для финальной строки

# Собираю строку в цикле, чтобы было красиво и кавычки прилегали вплотную к числу
for i in range(len(start_list)):
    if start_list[i].isdigit() or start_list[i][0] in '+-':
        final_sting += f'"{start_list[i]}" '
    elif '"' in start_list[i]:
        final_sting += ''
    else:
        final_sting += f' {start_list[i]} '

print(final_sting)
