n = int(input())

d = dict()
for i in range(n):
    a = input().split()
    for j in range(1, len(a)):
        d[a[j]] = a[0]

n = int(input())
for i in range(n):
    a = input()
    print(d[a])
