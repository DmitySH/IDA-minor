fin = open('input.txt', 'r', encoding='utf-8')

people = list()

for line in fin:
    sp_line = line.split()
    people.append((sp_line[0], sp_line[1], sp_line[3]))

people.sort(key=lambda x: x[0])
for x in people:
    print(*x)
