# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property
from abc import abstractmethod


class Clothes:
    cloth_all = 0

    def __init__(self, param):
        self.param = param
        result = self.cloth_counting
        Clothes.summon_cloth(self, result)

    @abstractmethod
    def cloth_counting(self):
        pass
    # Функция подсчитывает сколько всего надо ткани на всю одежду и сохранит в параметр .cloth_all
    def summon_cloth(self, result):
        Clothes.cloth_all += result


class Coat(Clothes):
    # Функция покажет сколько надо ткани непосредственно для пальто
    @property
    def cloth_counting(self):
        try:
            return int(self.param) / 6.5 + 0.5
        except ValueError:
            return f'Неверное значение {self.param}'


class Costume(Clothes):
    # Функция покажет сколько надо ткани непосредственно для костюма
    @property
    def cloth_counting(self):
        try:
            return int(self.param) * 2 + 0.3
        except ValueError:
            print(f'Неверное значение {self.param}')


coat_1 = Coat(58)
print(coat_1.cloth_counting)
print(coat_1.cloth_all)
print('*' * 40)

costume_1 = Costume(190)
print(costume_1.cloth_counting)
print(costume_1.cloth_all)
print('*' * 40)

costume_2 = Costume(180)
print(costume_2.cloth_all)
print('*' * 40)
