# Создать вручную список, содержащий цены на товары (10–20 товаров)
# A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
prices = [24, 8.99, 2.5, 11.4, 123, 1243.5, 4.1, 32.2, 85.1, 832.4, 12999, 1, 9]
task_res = 'task result: '  # Переменная для того чтобы не дублировать текст каждый раз
task_sep = "-" * 80  # После каждого ДЗ вставляется разделитель, чтобы результат скрипта лучше читался.

final_str = ''

for price in range(len(prices)):
    price = str(prices[price]).split(".")  # Каждую цену привожу к списку, разделитель "точка".
    if len(price) > 1:
        final_str += f' {int(price[0]):02} руб {int(price[1]):02} коп, '
    else:
        price.append('00')
        final_str += f'{int(price[0]):02} руб {price[1]} коп, '

print(f'"A" {task_res} \n{final_str}\n{task_sep}\n')

# B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что
# объект списка после сортировки остался тот же).
"""

"""
print(f'"B" {task_res}\nId before list became sorted - {id(prices)}\n')
prices.sort()

final_str = ''
for price in range(len(prices)):
    price = str(prices[price]).split(".")  # Каждую цену привожу к списку, разделитель "точка".
    if len(price) > 1:
        final_str += f'{int(price[0]):02} руб {int(price[1]):02} коп, '
    else:
        price.append('00')
        final_str += f'{int(price[0]):02} руб {price[1]} коп, '

print(f'{final_str}\n')
print(f'Id after list became sorted - {id(prices)} \n{task_sep}\n')

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
prices_list_from_max_to_min = prices[::-1]
final_str = ''

for price in range(len(prices_list_from_max_to_min)):
    price = str(prices_list_from_max_to_min[price]).split(".")  # Каждую цену привожу к списку, разделитель "точка".
    if len(price) > 1:
        final_str += f' {int(price[0]):02} руб {int(price[1]):02} коп, '
    else:
        price.append('00')
        final_str += f'{int(price[0]):02} руб {price[1]} коп, '

print(f'"C" {task_res} \nPrices list sorted in revers order:\n{final_str}\n{task_sep}\n')

# D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
final_str = ''

# По сути, код остался как и в остальных примерах, я взял список отсортированный в подзадании С и сделал
# срез до 5 элемента.
prices_list_from_max_to_min = prices_list_from_max_to_min[:5:]

for price in range(len(prices_list_from_max_to_min)):
    price = str(prices_list_from_max_to_min[price]).split(".")  # Каждую цену привожу к списку, разделитель "точка".
    if len(price) > 1:
        final_str += f' {int(price[0]):02} руб {int(price[1]):02} коп, '
    else:
        price.append('00')
        final_str += f'{int(price[0]):02} руб {price[1]} коп, '

print(f'"D" {task_res} \nTop-5 prices in prices list:\n{final_str}\n{task_sep}\n')
