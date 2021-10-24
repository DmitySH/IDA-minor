a = set()
b = set()
n, m = map(int, input().split())

for i in range(n):
    a.add(int(input()))
for j in range(m):
    b.add(int(input()))

both = a.intersection(b)
print(len(both))
print(*sorted(list(both)))
print(len(a.difference(b)))
print(*sorted(list(a.difference(b))))
print(len(b.difference(a)))
print(*sorted(list(b.difference(a))))
