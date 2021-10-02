a = list(map(int, input().split()))
prev = a[0]
for i in range(1, len(a)):
    if a[i] > prev:
        print(a[i])
    prev = a[i]
