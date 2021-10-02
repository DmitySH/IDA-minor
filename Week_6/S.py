def sum():
    n = int(input())
    s = 0
    while n != 0:
        s += n
        n = int(input())
    return s

print(sum())