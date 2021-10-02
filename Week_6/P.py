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


def ReduceFraction(n, m):
    k = gcd(n, m)
    return (n // k, m // k)


a, b = int(input()), int(input())
res = ReduceFraction(a, b)
print(res[0], res[1])
