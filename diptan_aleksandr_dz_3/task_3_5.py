from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_rand_number(input_list):
    """
    :param input_list: Получаем на вход список
    :return: возвращаем случайный элемент этого списка.
    """
    if len(input_list) > 0:
        return choice(input_list)


def get_joke(joke_count, no_repeat=False):
    jokes_list = []
    i = 0
    while i < joke_count:
        if no_repeat:
            joke_count = int(len(nouns)+4)  # Максимальное кол-во шуток уменьшаю, чтобы не было "пустых строк".
            noun = get_rand_number(nouns)  # Получаю случайное слово из списка
            adverb = get_rand_number(adverbs)
            adjective = get_rand_number(adjectives)
            joke = f'{noun} {adverb} {adjective}'
            jokes_list.append(joke)
            if len(nouns) > 0:  # перед удалением элемента списка, проверяю что список не пустой
                nouns.remove(noun)
            if len(adverbs) > 0:
                adverbs.remove(adverb)
            if len(adjectives) > 0:
                adjectives.remove(adjective)
        else:
            joke = f'{get_rand_number(nouns)} {get_rand_number(adverbs)} {get_rand_number(adjectives)}'
            jokes_list.append(joke)
        i += 1
    return jokes_list


print(get_joke(30,  no_repeat=True))
