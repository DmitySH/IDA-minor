total = 0
n = int(input())

for i in range(2, n + 1):
    print(i - 1, i, sep='*', end='')
    if i != n:
        print('+', end='')
    total += i * (i - 1)
print('=', total, sep='')
