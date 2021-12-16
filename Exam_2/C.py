shoes = list(map(int, input().split()))
legs = list(map(int, input().split()))

n = 0
legs.sort()
shoes.sort()
i = 0
j = 0
while i != len(legs) and j != len(shoes):
    if legs[i] <= shoes[j]:
        n += 1
        i += 1
        j += 1
    else:
        j += 1
print(n)
