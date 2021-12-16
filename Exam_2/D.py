import itertools as it

n = int(input())
s = list(map(int, input().split()))
total = 0

for x in it.combinations(s, 3):
    p = sum(x) / 2
    if p * (p - x[0]) * (p - x[1]) * (p - x[2]) > 0:
        total += 1
print(total)
