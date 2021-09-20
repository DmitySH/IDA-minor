num = int(input())
max = num
count = 1
while num != 0:
    num = int(input())
    if num != 0 and num > max:
        max = num
        count = 1
    elif num == max:
        count += 1
print(count)
