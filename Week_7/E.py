a = list(map(int, input().split()))

min1 = min(a[0], a[1])

min2 = (a[0] * a[1], a[0], a[1])

max1 = max(a[0], a[1])

max2 = (a[0] * a[1], a[0], a[1])

max3 = (a[0] * a[1] * a[2], a[0], a[1], a[2])

for x in a[2::]:
    if max3[0] < x * max2[0]:
        max3 = (x * max2[0], x, max2[1], max2[2])
    if max3[0] < x * min2[0]:
        max3 = (x * min2[0], x, min2[1], min2[2])

    if min2[0] > x * max1:
        min2 = (x * max1, x, max1)
    if min2[0] > x * min1:
        min2 = (x * min1, x, min1)

    if max2[0] < x * max1:
        max2 = (x * max1, x, max1)
    if max2[0] < x * min1:
        max2 = (x * min1, x, min1)

    max1 = max(max1, x)
    min1 = min(min1, x)

print(max3[1], max3[2], max3[3])
#-5 -4 1 2 3