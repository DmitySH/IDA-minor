a = list(map(int, input().split()))
k, x = map(int, input().split())
a.append(0)

for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = x
print(*a)
