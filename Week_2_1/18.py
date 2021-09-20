num = int(input())
if num != 0 and num % 2 == 0:
    i = 1
else:
    i = 0
while num != 0:
    num = int(input())
    if num != 0 and num % 2 == 0:
        i += 1
print(i)
