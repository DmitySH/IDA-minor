a = list(map(int, input().split()))

max_el = 1001

for i in range(len(a)):
    if (0 < a[i] < max_el):
        max_el = a[i]
print(max_el)
