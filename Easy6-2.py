# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Cars:
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

class TownCar(Cars):
    def __init__(self, speed, color, name, direction, is_police):
        Cars.__init__(self, speed, color, name, direction, is_police)

class SportCar(Cars):
    def __init__(self, speed, color, name, direction, is_police):
        Cars.__init__(self, speed, color, name, direction, is_police)

    def turbo(self):
        self.speed +=50

class WorkCar(Cars):
    def __init__(self, speed, color, name, direction, is_police, cargo_weight):
        Cars.__init__(self, speed, color, name, direction, is_police)
        self.cargo_weight = cargo_weight

class PoliceCar(Cars):
    def __init__(self, speed, color, name, direction, is_police, migalka):
        Cars.__init__(self, speed, color, name, direction, is_police)
        self.migalka = migalka

    def lyustra(self):
        if self.migalka == True:
            self.migalka = False
        elif self.migalka == False:
            self.migalka = True
            print('Vi-u-Vi-u-Vi-u')

TownCar1 = TownCar(50, 'red', 'Opel', 'Work', False)
print(TownCar1.speed)
print(TownCar1.direction)
TownCar1.go_accelerate()
TownCar1.turn()
print(TownCar1.speed)
print(TownCar1.direction)
TownCar1.stop()
print(TownCar1.speed)

SportCar1 = SportCar(75, 'purple', 'BMW', 'Home', False)
print(SportCar1.speed)
SportCar1.go_accelerate()
print(SportCar1.speed)
SportCar1.turbo()
print(SportCar1.speed)

PoliceCar1 = PoliceCar(60, 'yellow', 'Audi', 'Work', True, False)
print(PoliceCar1.migalka)
PoliceCar1.lyustra()
print(PoliceCar1.migalka)
