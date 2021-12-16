line = input()

n = 0
beg_syms = {';', ':'}
end_syms = {'(', ')', '[', ']'}
end = False

i = 0
while i < len(line):
    if line[i] in beg_syms:
        i += 1
        while i < len(line) and line[i] == '-':
            i += 1
        if i >= len(line):
            break
        if line[i] in end_syms:
            sym = line[i]
            while i < len(line) and line[i] == sym:
                i += 1
            n += 1
    else:
        i += 1

print(n)
