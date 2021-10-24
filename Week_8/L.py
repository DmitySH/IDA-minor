tels = set()

for i in range(4):
    n = input()
    res = ''
    for x in n:
        if x.isdigit():
            res = res + x
    if len(res) != 11:
        res = '8495' + res
    if res[0] == '7':
        res = '8' + res[1:]

    if i == 0:
        tels.add(res)
    else:
        if res in tels:
            print('YES')
        else:
            print('NO')
