n = int(input())
i = 1
while n % 2 == 0:
    n /= 2
if n == 1:
    print('YES')
else:
    print('NO')
