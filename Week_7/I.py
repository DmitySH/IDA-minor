s, n = map(int, input().split())
a = list()
for i in range(n):
    a.append(int(input()))
a.sort()
k = 0
for i in range(n):
    s -= a[i]
    if s <= 0:
        break
    else:
        k += 1
print(k)
