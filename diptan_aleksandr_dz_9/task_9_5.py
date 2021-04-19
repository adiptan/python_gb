class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли в руки {self.title}. Запуск отрисовки.')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли в руки {self.title}. Запуск отрисовки.')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли в руки {self.title}. Запуск отрисовки.')


pen = Pen('ручку')
pencil = Pencil('карандаш')
handle = Handle('маркер')
pen.draw()
pencil.draw()
handle.draw()
