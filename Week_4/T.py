s = input()
pos1 = s.find('h')
pos2 = s.rfind('h')

if not pos2 == pos1:
    s1 = s[pos1 + 1:pos2]
    s2 = s1.replace('h', 'H')
    s = s[:pos1 + 1] + s2 + s[pos2:]
    print(s)
else:
    print(s)
