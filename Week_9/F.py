d = dict()

with open('input.txt', 'r') as f:
    for line in f:
        for word in line.split():
            d[word] = d.get(word, 0) + 1

a = [(y, x) for x, y in d.items()]
for x in sorted(a, key=lambda x: (-x[0], x[1])):
    print(x[1])
