a = list(map(int, input().split()))
s = 1
prev = a[0]

for x in a:
    if x != prev:
        prev = x
        s += 1
print(s)
