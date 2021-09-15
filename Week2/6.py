n = int(input())

if 20 >= n >= 11 or 9 >= n % 10 >= 5 or n % 10 == 0:
    res = 'korov'
elif n % 10 == 1:
    res = 'korova'
elif n % 10 == 2 or 4 >= n % 10 >= 2:
    res = 'korovy'
print(n, res)
