def CountSort(a):
    values = [0] * 101
    for elem in a:
        values[elem] += 1
    i = 0
    j = 0
    for i in range(len(values)):
        if values[i] != 0:
            for k in range(values[i]):
                a[j] = i
                j += 1


a = list(map(int, input().split()))
CountSort(a)
print()
print(*a)
