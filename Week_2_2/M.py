num = int(input())
k = 0
while num != 0:
    prev = num
    num = int(input())

    if num != 0 and num > prev:
        k += 1
print(k)
