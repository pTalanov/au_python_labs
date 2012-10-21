__author__ = 'Pavel'


class SquareMatrix:

    def __init__(self, data):
        self.data = data
        self.size = len(data)
        for row in data:
            if self.size != len(row):
                raise AssertionError("Inconsistent data")

    def __getitem__(self, rowAndColumn):
        return self.data[rowAndColumn[0]][rowAndColumn[1]]

    def __setitem__(self, rowAndColumn, value):
        self.data[rowAndColumn[0]][rowAndColumn[1]] = value

    def __mul__(self, other):
        size = self.size
        assert size == other.size
        result = SquareMatrix.filledWithZeros(size)
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result[i, j] += self[i, k] * other[k, j]
        return result

    @staticmethod
    def filledWithZeros(size):
        data = []
        for i in range(size):
            data.append([])
            for j in range(size):
                data[i].append(0)
        return SquareMatrix(data)

    #not very pretty but who cares
    def __str__(self):
        repr = ""
        for i in range(self.size):
            for j in range(self.size):
                repr += str(self[i, j])
                if j != self.size - 1:
                    repr += " | "
            repr += "\n"
            if i != self.size - 1:
                for  j in range(self.size - 1):
                    repr += "----"
                repr += "-\n"
        return repr


if __name__ == '__main__':
    m1 = SquareMatrix([[1, 0, 1], [0, 1, 1], [0, 2, 1]])
    m2 = SquareMatrix([[0, 2, 1], [0, 2, 1], [0, 2, 1]])
    print(m1)
    print(m2)
    m3 = m1 * m2
    print(m3)



