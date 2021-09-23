p, x, y = float(input()), float(input()), float(input())
k = int(input())
i = 0

while i != k:
    i += 1
    summ = x * 100 + y
    summ += summ * (p / 100)
    x = int(summ // 100)
    y = int(summ % 100)
print(x, y)
