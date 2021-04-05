'''
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
'''

#Определяю константы
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

#Определяю список с секундами.
durations_in_sec = [320, 5604, 892, 65, 19680, 71235, 911235]

for duration in durations_in_sec:
    total_days = duration // SECONDS_IN_DAY
    total_hours = duration // SECONDS_IN_HOUR
    total_minutes = ((duration % SECONDS_IN_HOUR)//SECONDS_IN_MINUTE)
    total_seconds = duration % SECONDS_IN_MINUTE

    if duration < SECONDS_IN_MINUTE:
        print(duration)
    elif duration < SECONDS_IN_HOUR:
        print(f'{total_minutes} min, {total_seconds} sec')
    elif duration < SECONDS_IN_DAY:
        print(f'{total_hours} hours, {total_minutes} min, {total_seconds} sec')
    else:
        #Переопределяем переменную total_hours чтобы получить часы относительно прошедших дней
        total_hours = ((duration % SECONDS_IN_DAY)//SECONDS_IN_HOUR)
        print(f'{total_days} days, {total_hours} hours, {total_minutes} min, {total_seconds} sec')
