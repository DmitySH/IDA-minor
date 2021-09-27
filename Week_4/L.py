
def power(a, n):
    if n == 0:
        return 1
    if a == 0:
        return 0
    num = a
    for i in range(abs(n) - 1):
        a *= num
    if n < 0:
        return 1 / a
    else:
        return a


a, n = float(input()), int(input())
print(power(a, n))
