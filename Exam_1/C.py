n, m = list(map(int, input().split()))
k, p = list(map(int, input().split()))

for i in range(k, n + 1, k):
    for j in range(p, m + 1, p):
        if j < 10:
            sp = '0'
        else:
            sp = ''
        print(i, sp, j, sep='')
