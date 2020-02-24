class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title}.Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Идет запись с помощью инструмента {self.title}'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Идет рисование с помощью инструмента {self.title}'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выполняется выделение с помощью инструмента {self.title}'


pen = Pen('Ручка')
print(pen.title)
print(pen.draw())
pencil = Pencil('Карандаш')
print(pencil.title)
print(pencil.draw())
handle = Handle('Маркер')
print(handle.title)
print(handle.draw())
