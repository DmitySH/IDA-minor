n = int(input())

max_use = list(map(int, input().split()))

j = int(input())

pressed = list(map(int, input().split()))

for x in pressed:
    max_use[x - 1] -= 1

for x in max_use:
    if x >= 0:
        print('NO')
    else:
        print('YES')
