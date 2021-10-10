n = int(input())
a = list(map(int, input().split()))
x = int(input())
min_delta = 2001
closest = 0
for el in a:
    if abs(x - el) < min_delta:
        min_delta = abs(x - el)
        closest = el
print(closest)
