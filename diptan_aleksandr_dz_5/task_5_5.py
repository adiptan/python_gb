src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_numbers = set()
tmp_numbers = set()
for el in src:
    if el not in tmp_numbers:
        unique_numbers.add(el)
    else:
        unique_numbers.discard(el)
    tmp_numbers.add(el)

final_list = [el for el in src if el in unique_numbers]  # Создаю список на основе исходного, включаю все уникальные
# элементы из списка unique_numbers в том порядке, который был в исходноном списке
print(src)
print(final_list)
