n = int(input())
p = set(range(1, n + 1))
i = 0
while True:
    # i += 1
    # if i > 1000:
    #     raise Exception
    inp = input()
    if inp == 'HELP':
        break
    new = set(map(int, inp.split()))
    inp = input()

    if inp == 'YES':
        p &= new
    else:
        p -= new


print(*sorted(list(p)))
