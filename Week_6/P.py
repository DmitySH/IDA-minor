a = list(map(int, input().split()))
t1 = a.index(max(a))
t2 = a.index(min(a))
t3 = min(a)
t4 = max(a)

a[t1], a[t2] = t3, t4
print(*a)
