"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car rides')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        print(f'Car turned {direction}')

    def show_speed(self, speed):
        print(f'Car speed is {speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 60:
            print('TownCar Speed to high')
        else:
            print('Speed is good. Go ahead.')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 40:
            print('WorkCar Speed to high')
        else:
            print('Speed is good. Go ahead.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)


work_car = WorkCar(55, 'Brown', 'Work Car')
town_car = TownCar(32, 'Green', 'Town Car')
sport_car = SportCar(155, 'Yellow', 'Sport Car', True)
police_car = PoliceCar(145, 'Black', 'Police Car')
work_car.show_speed(32)
town_car.show_speed(55)
work_car.turn('Left')
town_car.turn('Right')
print(f'{town_car.name}, color: {town_car.color}, speed: {town_car.speed}')
print(f'{work_car.name}, color: {work_car.color}, speed: {work_car.speed}')
print(f'{sport_car.name}, color: {sport_car.color}, speed: {sport_car.speed}')
print(f'{police_car.name}, color: {police_car.color}, speed: {police_car.speed}')
