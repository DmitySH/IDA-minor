def merge(a, b):
    first = 0
    second = 0
    res = list()

    while first < len(a) and second < len(b):
        if a[first] <= b[second]:
            res.append(a[first])
            first += 1
        else:
            res.append(b[second])
            second += 1

    if first == len(a):
        for i in range(second, len(b)):
            res.append(b[i])
    else:
        for i in range(first, len(a)):
            res.append(a[i])

    return res

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
