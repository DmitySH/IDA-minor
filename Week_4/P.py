s = input()

pos = s.find('f')
if pos != -1:
    pos += 1
    pos = s.find('f', pos)
    print(pos)
else:
    print(-2)
