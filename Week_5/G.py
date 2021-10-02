a, b, c, d, e = int(input()), int(input()), int(input()), \
                int(input()), int(input())

k = 0
for x in range(1001):
    if x - e != 0:
        if (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
            k += 1
print(k)
