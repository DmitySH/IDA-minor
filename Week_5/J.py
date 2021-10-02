n = int(input())

prod = 1
s = 0
for i in range(1, n + 1):
    prod *= i
    s += prod

print(s)