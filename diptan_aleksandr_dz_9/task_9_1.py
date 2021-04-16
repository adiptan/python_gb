from time import sleep


class TrafficLight:
    __color = ''

    def running(self, color, seconds_for_timer):
        TrafficLight.__color = color
        self.seconds_for_timer = seconds_for_timer
        print(f'Color is {color}')
        for i in range(seconds_for_timer, 0, -1):
            print(i)
            sleep(1)


a = TrafficLight()
a.running('Red', 7)
print(a._TrafficLight__color)  # Проверяю, что аттрибут переопределился
a.running('Yellow', 2)
print(a._TrafficLight__color)
a.running('Green', 5)
print(a._TrafficLight__color)
