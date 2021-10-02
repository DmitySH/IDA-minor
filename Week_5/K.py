n = int(input())
s1 = 0
s2 = 0

for i in range(1, n):
    s1 += int(input())
    s2 += i
print(s2 + n - s1)
