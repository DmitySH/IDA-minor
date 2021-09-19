num = int(input())
count = 1
prev = num
max_row = 1
while num != 0:
    num = int(input())
    if num != 0 and num == prev:
        count += 1
    if num != prev and num != 0:
        if count > max_row:
            max_row = count
        count = 1
        prev = num
if max_row < count:
    print(count)
else:
    print(max_row)
