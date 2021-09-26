s = input()
res = ''
i = 0
for sym in s:
    if i % 3 != 0:
        res += sym
    i += 1
print(res)
