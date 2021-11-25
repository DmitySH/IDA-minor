import copy
from sys import stdin
from functools import *


class Matrix:
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

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])


exec(stdin.read())
