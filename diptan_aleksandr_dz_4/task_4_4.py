#Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать
# скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.
import utils

print(f'Rate for USD is {utils.currency_rates("Usd")}')
print(f'Rate for EUR is {utils.currency_rates("EuR")}')
print(f'Rate for TUG is {utils.currency_rates("TUG")}')
