class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        print('Площадь ткани для пальто:')
        return self.width / 6.5 + 0.5

    def get_square_s(self):
        print('Площадь ткани для костюма:')
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3))}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто {self.square_c}'


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм {self.square_s}'


coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.get_sq_full)
print(suit.get_sq_full)
print(coat.get_square_c())
print(suit.get_square_s())
