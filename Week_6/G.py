a = list(map(int, input().split()))

max_el = a[0]
ind = 0

for i in range(1, len(a)):
    if (a[i] > max_el):
        max_el = a[i]
        ind = i
print(max_el, ind)
