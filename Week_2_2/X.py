n = int(input())
k = 0
a = list()
s = 0

while n != 0:
    a.append(n)
    s += n

    n = int(input())
    k += 1

i = 0
sa = s / k
ss = 0
while i != k:
    ss += (a[i] - sa) ** 2
    i += 1
print((ss/(k - 1)) ** (1/2))
