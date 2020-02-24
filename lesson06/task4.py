class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} started moving'

    def stop(self):
        return f'{self.name} stopped'

    def turn_left(self):
        return f'{self.name} turned left'

    def turn_right(self):
        return f'{self.name} turned right'

    def show_speed(self):
        return f'{self.name} speed is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')
        if self.speed > 60:
            return f'Your speed is higher than limit'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')
        if self.speed > 40:
            return f'Your speed is higher than limit'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


ferrari = SportCar(250, 'red', 'ferrari', False)
kia = TownCar(80, 'black', 'kia', False)
pickup = WorkCar(40, 'gray', 'pickup', False)
ford = PoliceCar(100, 'black/white', 'ford', True)

print(ferrari.show_speed())
print(kia.show_speed())
print(ford.go())
print(pickup.turn_right())
