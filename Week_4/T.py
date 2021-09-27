from math import sqrt


def cycle(n, had_sqr):
    if n != 0:
        cycle(int(input()), had_sqr)
    if n > 0:
        if (sqrt(n).is_integer()):
            print(n, end=' ')
            had_sqr = True
        return had_sqr


if not cycle(int(input()), False):
    print(0)
