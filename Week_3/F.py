n = float(input())
n *= 100
x = int(n // 100)
y = int(n % 100)
if int(n // 10 % 10) == 0 and int(n % 10) == 0:
    print(x, ' ', int(n % 10), sep='')
else:
    print(x, ' ', int(n // 10 % 10), int(n % 10), sep='')
