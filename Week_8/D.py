a = list(map(int, input().split()))
b = set()
for x in a:
    if x in b:
        print('YES')
    else:
        print('NO')
        b.add(x)
