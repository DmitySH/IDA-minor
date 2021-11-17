import itertools

print('\n'.join(
    map(lambda x: str(x).replace(',', '').replace('(', '').replace(')',
                                                                   '').replace(
        ' ', ''), itertools.permutations(range(1, int(input()) + 1)))))
