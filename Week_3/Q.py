n = int(input())
cur = 1
prev = 0
i = 1
while cur < n:
    i += 1
    cur, prev = cur + prev, cur
if cur == n:
    print(i)
else:
    print(-1)
