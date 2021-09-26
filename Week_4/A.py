def min4(a, b, c, d):
    return min(min(min(a, b), c), d)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min4(a, b, c, d))
