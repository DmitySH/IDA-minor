from math import sqrt


def IsPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
