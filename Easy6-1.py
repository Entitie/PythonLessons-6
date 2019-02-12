# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, speed, color, name, direction, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police

    def go_accelerate(self):
        self.speed += 10

    def stop(self):
        self.speed = 0

    def turn(self):
        '''Машина ездит между домом и работой, запуск функции будет её разворачивать'''
        if self.direction == 'Work':
            self.direction = 'Home'
        elif self.direction == 'Home':
            self.direction = 'Work'

class SportCar:
    def __init__(self, speed, color, name, direction, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police

    def go_accelerate(self):
        self.speed += 10

    def turbo(self):
        self.speed +=50

    def stop(self):
        self.speed = 0

    def turn(self):
        '''Машина ездит между домом и работой, запуск функции будет её разворачивать'''
        if self.direction == 'Work':
            self.direction = 'Home'
        elif self.direction == 'Home':
            self.direction = 'Work'

class WorkCar:
    def __init__(self, speed, color, name, direction, is_police, weight):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police
        self.weight = weight

    def go_accelerate(self):
        self.speed += 10

    def stop(self):
        self.speed = 0

    def turn(self):
        '''Машина ездит между домом и работой, запуск функции будет её разворачивать'''
        if self.direction == 'Work':
            self.direction = 'Home'
        elif self.direction == 'Home':
            self.direction = 'Work'

class PoliceCar:
    def __init__(self, speed, color, name, direction, is_police, migalka):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police
        self.migalka = migalka

    def go_accelerate(self):
        self.speed += 10

    def stop(self):
        self.speed = 0

    def lyustra(self):
        if self.migalka == 1:
            self.migalka = 0
        elif self.migalka == 0:
            self.migalka = 1

    def turn(self):
        '''Машина ездит между домом и работой, запуск функции будет её разворачивать'''
        if self.direction == 'Work':
            self.direction = 'Home'
        elif self.direction == 'Home':
            self.direction = 'Work'

TownCar1 = TownCar(50, 'red', 'Opel', 'Work', False)
print(TownCar1.speed)
print(TownCar1.direction)
TownCar1.go_accelerate()
TownCar1.turn()
print(TownCar1.speed)
print(TownCar1.direction)
TownCar1.stop()
print(TownCar1.speed)
