n = int(input())

i = 1
k = 0
while i != n + 1:
    a = i
    rev = 0
    while a != 0:
        rev = rev * 10 + a % 10
        a //= 10

    if i == rev:
        k += 1
    i += 1
print(k)
