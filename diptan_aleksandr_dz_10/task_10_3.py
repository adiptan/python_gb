class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)


cells1 = Cell(8)
cells2 = Cell(22)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells1 / cells2)
