'''
 A. Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
 Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать
 в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
'''
list_with_digits = [i**3 for i in range(1000) if i % 2 != 0]

total_sum_numbers = 0

for i in list_with_digits:
    z = i
    sum_of_number = 0
    while i > 0:
        sum_of_number = i % 10 + sum_of_number
        i = i // 10
    if sum_of_number % 7 == 0:
        total_sum_numbers = total_sum_numbers + z

print(total_sum_numbers)

'''
 B. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
'''
SEVENTINE = 17
list_with_digits = [i**3 for i in range(1000) if i % 2 != 0]

total_sum_numbers = 0

for i in list_with_digits:
    i = i + SEVENTINE
    z = i
    sum_of_number = 0
    while i > 0:
        sum_of_number = i % 10 + sum_of_number
        i = i // 10
    if sum_of_number % 7 == 0:
        total_sum_numbers = total_sum_numbers + z

print(total_sum_numbers)

'''
 C. * Решить задачу под пунктом b, не создавая новый список.
'''
#Я изначально не создавал второй список. Это считается выполнением подзадания С* ?
