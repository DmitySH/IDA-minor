a = int(input())
b = int(input())
n = int(input())

rub = (b * n + a * 100 * n) // 100
cop = (b * n + a * 100 * n) % 100
print(rub, cop)
