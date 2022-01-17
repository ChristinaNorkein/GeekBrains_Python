class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала...')

    def stop(self):
        print(f'{self.name} остановилась...')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}...')

    def show_speed(self):
        print(f'Разгоняется до скорости: {self.speed}...')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 100:
            print(f'При скорости {self.speed} км/ч по городу будет выписан штраф!')
        else:
            print(f'Максимально допустимая скорость по городу - 100 км/ч.')

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'При скорости {self.speed} км/ч по городу будет выписан штраф!')
        else:
            print(f'Максимально допустимая скорость грузовиков по городу - 60 км/ч.')

class PoliceCar(Car):

    def it_police(self):
        if self.is_police == True:
            print(f'{self.name} с мигалками, так как является полицейской.')
        else:
            print(f'Похоже {self.name} не является полицейской машиной...')

new_car = PoliceCar('BMW', 'Синий', 125, True)
new_car.go()
new_car.turn('направо')
new_car.show_speed()
new_car.it_police()
