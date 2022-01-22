class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.list)):
            sum_matrix.append([])
            for j in range(len(self.list[0])):
                sum_matrix[i].append(self.list[i][j] + other.list[i][j])
        return '\n'.join(map(str, sum_matrix))


obj1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
obj2 = [[3, 5, 8], [8, 3, 7], [3, 1, 31]]

matrix_1 = Matrix(obj1)
matrix_2 = Matrix(obj2)

print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)
