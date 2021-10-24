d = dict()

total = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        d[line] = d.get(line, 0) + 1
        total += 1

a = [(y, x) for x, y in d.items()]
a.sort(key=lambda x: (-x[0], x[1]))
if a[0][0] > total / 2:
    print(a[0][1])
else:
    print(a[0][1])
    print(a[1][1])
