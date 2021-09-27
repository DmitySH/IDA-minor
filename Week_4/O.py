def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if a > b:
        a = a % b
    else:
        b = b % a
    return gcd(a, b)


a, b = int(input()), int(input())
print(gcd(a, b))
