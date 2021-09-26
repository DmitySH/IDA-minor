s = input()
res = ''
for sym in s:
    res += sym + '*'
print(res[:len(res) - 1])
