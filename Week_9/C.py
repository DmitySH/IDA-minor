n = int(input())
d = dict()

for i in range(n):
    synonyms = input().split()
    d[synonyms[0]] = synonyms[1]
    d[synonyms[1]] = synonyms[0]
print(d[input()])
