n = int(input())
aall = set()
every = set()
for i in range(n):
    m = int(input())
    new = set()
    for j in range(m):
        lang = input()
        aall.add(lang)
        if i == 0:
            every.add(lang)
        new.add(lang)
    every &= new
print(len(every))
for x in every:
    print(x)

print(len(aall))
for x in aall:
    print(x)
