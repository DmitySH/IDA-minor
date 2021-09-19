n = int(input())
cur = 1
prev = 0
i = 0
while i != n - 1:
    i += 1
    cur, prev = cur + prev, cur
print(cur)
