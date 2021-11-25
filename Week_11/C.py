import copy
from sys import stdin
from functools import *


class MatrixError(Exception):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:

    @classmethod
    def transposed(cls, matrix):
        lines = list()
        for j in range(matrix.size()[1]):
            line = list()
            for i in range(matrix.size()[0]):
                line.append(matrix[i][j])
            lines.append(line)
        return Matrix(lines)

    def __init__(self, ar):
        self.__matrix = list()
        for line in ar:
            new_line = list()
            for elem in line:
                new_line.append(copy.deepcopy(elem))
            self.__matrix.append(new_line)

    def __str__(self):
        res = '\n'.join(map(lambda x: reduce(lambda t, y: str(t) + '\t' + str(y), x), self.__matrix))
        return res

    def __getitem__(self, key):
        return self.__matrix[key]

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])

    def __add__(self, other):
        if self.size()[0] != other.size()[0] or self.size()[1] != other.size()[1]:
            raise MatrixError(self, other)

        lines = list()
        for i in range(self.size()[0]):
            line = list()
            for j in range(self.size()[1]):
                line.append(self[i][j] + other[i][j])
            lines.append(line)
        return Matrix(lines)

    def transpose(self):
        lines = list()
        for j in range(self.size()[1]):
            line = list()
            for i in range(self.size()[0]):
                line.append(self[i][j])
            lines.append(line)
        self.__matrix = lines
        return Matrix(lines)

    def __mul__(self, other):
        lines = list()
        for i in range(self.size()[0]):
            line = list()
            for j in range(self.size()[1]):
                line.append(self[i][j] * other)
            lines.append(line)
        return Matrix(lines)

    __rmul__ = __mul__


exec(stdin.read())
