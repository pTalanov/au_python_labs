import unittest

import matrix
import math

class MatrixTest(unittest.TestCase):

    def testConstructor(self):
        m1 = matrix.Matrix([1, 1, 1, 2, 1, 1, 1, 3, 1])
        m2 = matrix.Matrix([[1, 1, 1], [2, 1, 1], [1, 3, 1]])
        assert m1 == m2

    def testGetSetItem(self):
        m1 = matrix.Matrix([1, 1, 1, 2, 1, 1, 1, 3, 1])
        assert m1[2, 1] == 3
        m1[2, 0] = 4
        assert m1 == matrix.Matrix([1, 1, 1, 2, 1, 1, 4, 3, 1])

    def testAdd(self):
        m1 = matrix.Matrix([1, 1, 1, 2, 1, 1, 1, 3, 1])
        m2 = matrix.Matrix([[2, 1, 1], [2, 4, 1], [1, 3, 2]])
        m3 = m1 + m2
        assert m3 == matrix.Matrix([3, 2, 2, 4, 5, 2, 2, 6, 3])

    def testMul(self):
        list = [1, 1, 1, 2, 1, 1, 1, 3, 1]
        m1 = matrix.Matrix(list)
        assert m1 * matrix.Matrix.identity() == m1
        assert m1 * m1 == matrix.Matrix([4, 5, 3, 5, 6, 4, 8, 7, 5])

        assert m1 * 3 == matrix.Matrix([i * 3 for i in list])
        zeroVector = matrix.Vector([0, 0, 0])
        assert m1 * zeroVector == zeroVector
        assert m1 * matrix.Vector([1, 1, 1]) == matrix.Vector([3, 4, 5])

    def testRotation(self):
        v = matrix.Vector([1, 0, 0])
        z = matrix.RotationMatrix(math.pi / 2)
        assert matrix.Vector([round(i, 5) for i in (z * v).data]) == matrix.Vector([0, 1, 0])
