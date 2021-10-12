distances = list(map(int, input().split()))
price = list(map(int, input().split()))

distances.sort(key=lambda x: -x)
price.sort()

s = 0
for i in range(len(distances)):
    s += distances[i] * price[i]
print(s)
