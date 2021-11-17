import itertools

print(*itertools.accumulate(list([1] + list(range(1, int(input()) + 1))),
                            lambda x, y: x * y))
