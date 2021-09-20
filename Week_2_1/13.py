a, b = int(input()), int(input())
cur = a
day = 1
while a < b:
    a *= 1.1
    day += 1
print(day)
