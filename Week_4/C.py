from math import *

def my_len(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

a, b, c, d, e, f = int(input()), int(input()), int(input()), int(input()),\
                   int(input()), int(input())
print(my_len(a, b, c, d) + my_len(e, f, c, d) + my_len(a, b, e, f))
