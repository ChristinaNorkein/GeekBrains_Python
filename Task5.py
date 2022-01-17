class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):

    def draw(self):
        print(f'{self.title} рисует синими чернилами.')

class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} имеет мягкий грифель.')

class Handle(Stationery):

    def draw(self):
        print(f'{self.title} - используй его для отрисовки границ.')


tool = Handle('Черный маркер')
tool.draw()
