import math

SIZE = 3

class Vector:

    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return ",".join([str(i) for i in self.data])


class Matrix():

    def __init__(self, list):

        if len(list) == SIZE:
            self.data = list
        else:
            self.data = [list[SIZE * i : SIZE * i + SIZE] for i in range(0, SIZE)]

    def _asList(self):
        res = []
        for row in self.data:
            res.extend(row)
        return res

    def __eq__(self, other):
        return self.data == other.data

    def __mul__(self, other):

        if isinstance(other, Vector):
            res = [0, 0, 0]
            for i in range(SIZE):
                for j in range(SIZE):
                    res[i] += self[i, j] * other[j]
            return Vector(res)


        if isinstance(other, Matrix):
            res = Matrix.filledWithZeros()
            for i in range(SIZE):
                for j in range(SIZE):
                    for k in range(SIZE):
                        res[i , j] += self[i, k] * other[k, j]
            return res

        return Matrix([self[i] * other for i in Matrix.indices()])


    def __getitem__(self, rowAndColumn):
        return self.data[rowAndColumn[0]][rowAndColumn[1]]

    def __setitem__(self, rowAndColumn, value):
        self.data[rowAndColumn[0]][rowAndColumn[1]] = value

    def __add__(self, other):
        return Matrix([self[i] + other[i] for i in Matrix.indices()])

    @staticmethod
    def filledWithZeros():
        return Matrix([0 for i in range(SIZE * SIZE)])

    @staticmethod
    def identity():
        return Matrix([[1 if x == y  else 0 for x in range(SIZE)] for y in range(SIZE)])

    @staticmethod
    def indices():
        return [(i // SIZE, i % SIZE) for i in range(9)]


class RotationMatrix(Matrix):
    def __init__(self, angle):
        data = [[math.cos(angle), -math.sin(angle), 0],
                [math.sin(angle), math.cos(angle), 0],
                [0, 0, 1]]

        super().__init__(data)



