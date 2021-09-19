n = int(input())
prev = 0
prev_prev = 0
if n != 0:
    prev = n
    n = int(input())
    if n != 0:
        prev_prev, prev = prev, n

lmf = 0
lms = 0

d = 0
i = 1
while n != 0:
    n = int(input())

    if n != 0 and prev > n and prev > prev_prev and lmf == 0:
        lmf = i
        i += 1
        prev, prev_prev = n, prev
        continue

    if n != 0 and prev > n and prev > prev_prev and lmf != 0 and lms == 0:
        lmf, lms = i, lmf
        d = lmf - lms
        i += 1
        prev, prev_prev = n, prev
        continue

    if n != 0 and prev > n and prev > prev_prev and lmf != 0 and lms != 0:
        lmf, lms = i, lmf
        if d > lmf - lms:
            d = lmf - lms
    prev, prev_prev = n, prev
    i += 1

if lms == 0 or lmf == 0:
    print(0)
else:
    print(d)
