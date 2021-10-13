fin = open('input.txt', 'r', encoding='utf-8')

maxs = [[0, 0], [0, 0], [0, 0]]

for line in fin:
    sp_line = list(map(int, line.split()[2:]))

    if maxs[sp_line[0] - 9][0] < sp_line[1]:
        maxs[sp_line[0] - 9][1] = maxs[sp_line[0] - 9][0]
        maxs[sp_line[0] - 9][0] = sp_line[1]
    elif maxs[sp_line[0] - 9][1] < sp_line[1] and sp_line[1] != maxs[sp_line[0] - 9][0]:
        maxs[sp_line[0] - 9][1] = sp_line[1]

for x in maxs:
    print(x[1], end=' ')
