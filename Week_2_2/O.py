num = int(input())
max = num
k = 1
while num != 0:
    num = int(input())
    if num != 0 and num == max:
        k += 1
    if num != 0 and num > max:
        max = num
        k = 1

print(k)
