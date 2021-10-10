a = list(map(int, input().split()))

mmax = (a[0], 0)

for i in range(1, len(a)):
    if a[i] >= mmax[0]:
        mmax = (a[i], i)

print(*mmax)
