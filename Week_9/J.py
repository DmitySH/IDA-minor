d = dict()
total = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split()
        party_name = line[:len(line) - len(words[-1]) - 2]
        d[party_name] = d.get(party_name, 0) + int(words[-1])
        total += int(words[-1])

pich = total / 450

res = dict()

s = 0
for x in d:
    res[(-(d[x] / pich - int(d[x] / pich)), d[x], x)] = int(d[x] / pich)
    s += int(d[x] / pich)

s = 450 - s
for x in sorted(res):
    if s <= 0:
        break
    res[x] += 1
    s -= 1

for x in res:
    print(x[2], res[x])
