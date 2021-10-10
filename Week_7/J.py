a = list(map(int, input().split()))
p = int(input())

for i in range(len(a)):
    if p > a[i]:
        print(i + 1)
        break
else:
    print(len(a) + 1)
