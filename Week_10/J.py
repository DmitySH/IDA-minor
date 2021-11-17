import functools

print(*map(lambda x: functools.reduce(lambda z, y: int(z) ^ int(y), x),
           zip(*list(map(lambda x: input().split(), range(int(input()))))[
                ::-1])))
