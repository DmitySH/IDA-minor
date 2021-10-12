a = list()

n = int(input())

for i in range(n):
    family, score = input().split()
    a.append((family, int(score)))

a.sort(key=lambda x: -x[1])

for man in a:
    print(man[0])
