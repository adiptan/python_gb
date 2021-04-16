class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self.centimeters = 0.005
        self.weight = 25
        self._length = length
        self._width = width

    def calculation(self):
        total = self._length * self._width * self.weight * self.centimeters
        print(f'It is need {total} tons of asphalt for the road building')


road_to_the_bright_future = Road(20000, 30)
road_to_the_bright_future.calculation()
