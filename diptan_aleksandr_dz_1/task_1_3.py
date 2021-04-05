'''
Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
'''
for percent in range(21):
    if percent == 0:
        print(f'{percent} процентов')
    elif percent == 1:
        print(f'{percent} процент')
    elif percent < 5:
        print(f'{percent} процента')
    else:
        print(f'{percent} процентов')