class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')

    def get_total_income(self):
        print(f'Доход: {sum(self._income.values())}')


employee = Position('Томас', 'Андерсон', 'junior programmer', 5000, 3000)
employee.get_full_name()
print(f'Должность: {employee.position}')
employee.get_total_income()
