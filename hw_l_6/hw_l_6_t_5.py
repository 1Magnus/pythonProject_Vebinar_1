# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. - Pen')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. - Pencil')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. - Handle')


stationery_1 = Stationery('Циркуль')
print(stationery_1.title)
stationery_1.draw()

pen_1 = Pen('Синяя ручка')
print(pen_1.title)
pen_1.draw()

pencil_1 = Pencil('Зеленый карандаш')
print(pencil_1.title)
pencil_1.draw()

handle_1 = Handle('Красный маркер')
print(handle_1.title)
handle_1.draw()
