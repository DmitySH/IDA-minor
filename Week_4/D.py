def xor(x, y):
    if x == 1 and y == 0 or y == 1 and x == 0:
        return 1
    else:
        return 0

x, y = int(input()), int(input())
print(xor(x, y))
