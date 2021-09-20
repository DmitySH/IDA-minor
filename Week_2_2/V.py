n = int(input())

a = list()
i = 1
a.append(n)
row_bigger = 0
row_less = 0
row = 1
while n != 0:
    n = int(input())
    if n == 0:
        break
    a.append(n)
    if n > a[i - 1]:
        row += 1
    else:
        if row > row_bigger:
            row_bigger = row
        row = 1
    i += 1

if row > row_bigger:
    row_bigger = row

row = 0
i = 0
a.reverse()
while i < len(a):
    if a[i] > a[i - 1]:
        row += 1
    else:
        if row > row_less:
            row_less = row
        row = 1
    i += 1
if row > row_less:
    row_less = row

if row_bigger > row_less:
    print(row_bigger)
else:
    print(row_less)
