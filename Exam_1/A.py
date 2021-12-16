t = list(map(int, input().split()))

res = (t[0] * 100 + t[1]) * t[2]
print(res // 100, res % 100)
