a = list(map(int, input().split()))

k = 0
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i])
