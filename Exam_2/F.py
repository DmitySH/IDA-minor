def transpose(a):
    n = len(a)
    new_a = list()
    for i in range(n):
        line = list()
        for j in range(n):
            line.append(a[j][i])
        new_a.append(line)
    return new_a


a = list()

n, k = map(int, input().split())

for i in range(n):
    line = list(map(int, input().split()))
    a.append(line)

a = transpose(a)

for i in range(n):
    for j in range(n):
        a[i][j] = (abs(a[i][j] - k), a[i][j])

for x in a:
    x.sort()

a = transpose(a)
for i in range(n):
    for j in range(n):
        print(a[i][j][1], end=' ')
    print()
