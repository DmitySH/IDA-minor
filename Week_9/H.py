d = dict()

with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split()
        if words[0] not in d:
            d[words[0]] = dict()

        d[words[0]][words[1]] = d[words[0]].get(words[1], 0) + int(words[2])


for buyer in sorted(d):
    print(buyer + ':')
    for x in sorted(d[buyer]):
        print(x, d[buyer][x])
