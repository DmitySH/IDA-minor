s = input()
pos1 = s.find('h')
pos2 = s.rfind('h')

s1 = s[pos1 + 1:pos2]
s2 = s1.replace('h', 'H')
print(s.replace(s1, s2))
