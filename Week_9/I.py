d = dict()

with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split()
        if words[0] == 'DEPOSIT':
            d[words[1]] = d.get(words[1], 0) + int(words[2])
        elif words[0] == 'WITHDRAW':
            d[words[1]] = d.get(words[1], 0) - int(words[2])
        elif words[0] == 'BALANCE':
            if words[1] in d:
                print(d[words[1]])
            else:
                print('ERROR')
        elif words[0] == 'TRANSFER':
            d[words[1]] = d.get(words[1], 0) - int(words[3])
            d[words[2]] = d.get(words[2], 0) + int(words[3])
        elif words[0] == 'INCOME':
            for user, balance in d.items():
                if balance > 0:
                    d[user] += int(int(words[1]) / 100 * d[user])