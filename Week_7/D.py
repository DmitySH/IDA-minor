a = list(map(int, input().split()))
minus_max1 = 1
minus_max2 = 1
plus_max1 = -1
plus_max2 = -1

for x in a:
    if x <= 0 and minus_max1 > x:
        minus_max2 = minus_max1
        minus_max1 = x
    elif x <= 0 and minus_max2 > x:
        minus_max2 = x
    if x >= 0 and plus_max1 < x:
        plus_max2 = plus_max1
        plus_max1 = x
    elif x >= 0 and plus_max2 < x:
        plus_max2 = x
if minus_max1 * minus_max2 > plus_max2 * plus_max1:
    if minus_max1 > minus_max2:
        print(minus_max2, minus_max1)
    else:
        print(minus_max1, minus_max2)
else:
    if plus_max1 > plus_max2:
        print(plus_max2, plus_max1)
    else:
        print(plus_max1, plus_max2)
