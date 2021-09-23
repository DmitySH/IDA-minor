s = input()
pos1 = s.find('h')
pos2 = s.rfind('h')

s1 = s[pos1:pos2 + 1]
print(s.replace(s1, ''))
