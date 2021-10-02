a = list(map(int, input().split()))

max_el = 2

for i in range(len(a)):
    if a[i] % 2 == 1 and max_el == 2:
        max_el = a[i]
    if a[i] % 2 == 1 and a[i] < max_el and max_el != 2:
        max_el = a[i]
print(max_el)
