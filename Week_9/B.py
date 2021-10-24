d = dict()

with open('input.txt', 'r') as f:
    for line in f:
        for word in line.split():
            if word not in d:
                d[word] = 0
            else:
                d[word] += 1
            print(d[word], end=' ')
