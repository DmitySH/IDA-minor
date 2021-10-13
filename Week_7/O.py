fin = open('input.txt', 'r', encoding='utf-8')

maxs = [0, 0, 0]

for line in fin:
    sp_line = list(map(int, line.split()[2:]))

    if maxs[sp_line[0] - 9] < sp_line[1]:
        maxs[sp_line[0] - 9] = sp_line[1]

print(*maxs)
