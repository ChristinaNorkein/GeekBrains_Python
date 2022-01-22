class Cage:

    def __init__(self, lot):
        self.lot = lot

    def __add__(self, other):
        return self.lot + other.lot

    def __sub__(self, other):
        result = self.lot - other.lot
        if result > 0:
            return result
        else:
            return 'Результат меньше 0.'

    def __mul__(self, other):
        return self.lot * other.lot

    def __truediv__(self, other):
        return self.lot / other.lot

    def make_order(self, x):
        return '\n'.join(['@' * x for el in range(self.lot // x)]) + '\n' + '@' * (self.lot % x)


cage_1 = Cage(45)
cage_2 = Cage(90)
cage_3 = Cage(15)

print(f'Сложение: {cage_1 + cage_2}')
print(f'Вычитание: {cage_1 - cage_2}')
print(f'Умножение: {cage_1 * cage_2}')
print(f'Деление: {cage_1 / cage_2}')
print(cage_3.make_order(4))
