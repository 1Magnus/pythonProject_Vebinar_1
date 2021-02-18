# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула
# (куда).# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов и также покажите результат.

class Auto:
    def __init__(self, color, name, speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Повернула - {direction}')

    def show_speed(self):
        print(f'Скорость ровна = {self.speed}')


class TownCar(Auto):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, is_police, speed)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена! на {self.speed - 60}')
        else:
            print(f'Скорость ровна = {self.speed}')


class SportCar(Auto):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, speed, is_police)



class WorkCar(Auto):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, is_police, speed)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена! на {self.speed - 40}')
        else:
            print(f'Скорость ровна = {self.speed}')


class PoliceCar(Auto):
    def __init__(self, color, name, speed=0, is_police=True):
        super().__init__(color, name, speed)
        self.is_police = is_police


town_car_1 = TownCar('Green', 'Вася')
print(town_car_1.name, town_car_1.color)
town_car_1.go()
town_car_1.speed = 100
town_car_1.show_speed()
town_car_1.turn('Left')
town_car_1.stop()

sport_car_1 = SportCar('Red', 'Николай')
print(sport_car_1.name, sport_car_1.color)
sport_car_1.go()
sport_car_1.speed = 120
sport_car_1.show_speed()
sport_car_1.turn('Right')
sport_car_1.stop()

work_car_1 = WorkCar('Black', 'Вася')
print(work_car_1.name, work_car_1.color)
work_car_1.go()
work_car_1.speed = 100
work_car_1.show_speed()
work_car_1.turn('Left')
work_car_1.stop()

police_car_1 = PoliceCar('Red', 'Николай')
print(police_car_1.name, police_car_1.color, f'Полицейская - {police_car_1.is_police}')
police_car_1.go()
police_car_1.speed = 120
police_car_1.show_speed()
police_car_1.turn('Right')
police_car_1.stop()
