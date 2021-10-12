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


size = int(input())
a = list(map(int, input().split()))

CountSort(a)

k = 0

for shoe in a:
    if size <= shoe:
        k += 1
        size = shoe + 3

print(k)
