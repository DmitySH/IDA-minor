s = input()
pos = s.find('f')

if pos != -1:
    print(pos, end=' ')
    pos += 1
if s.find('f', pos) != -1:
    print(s.rfind('f'))
