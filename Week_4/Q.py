s = input()
pos1 = s.find('h')
pos2 = s.rfind('h')

s1 = s[:pos1] + s[pos1:pos2] + s[pos1 + 1:pos2 + 1] + s[pos2 + 1:]
print(s1)
