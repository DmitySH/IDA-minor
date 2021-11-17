import math

print(*filter(
    lambda y: all(map(lambda x: y % x != 0, range(2, int(math.sqrt(y)) + 1))),
    range(2, int(input()) + 1)))
