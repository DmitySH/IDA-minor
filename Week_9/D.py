d = dict()
mmax = 0

with open('input.txt', 'r') as f:
    for line in f:
        for word in line.split():
            d[word] = d.get(word, 0) + 1
            if d[word] > mmax:
                mmax = d[word]

for x in sorted(d):
    if d[x] == mmax:
        print(x)
        break
