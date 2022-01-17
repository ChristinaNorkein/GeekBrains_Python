class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        return f'{self._length}м * {self._width}м * 25кг * 5см = {(self._length * self._width * 25 * 5) / 1000}т'


road_result = Road(7000, 50)
print(road_result.massa())
