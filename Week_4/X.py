from math import sqrt


def cycle(had_sqr):
    n = int(input())
    if n != 0:
        had_sqr = cycle(had_sqr)
    if n > 0:
        if (sqrt(n).is_integer()):
            print(n, end=' ')
            had_sqr = True
        return had_sqr

if not cycle(False):
    print(0, '')
