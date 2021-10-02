a, b = int(input()), int(input())

sign = 1
if b < a:
    sign = -1

for i in range(a, b + sign, sign):
    print(i)
