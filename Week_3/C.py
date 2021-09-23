import math

a, b, c = float(input()), float(input()), float(input())
p = 0.5 * (a + b + c)
print(math.sqrt(p*(p-a)*(p-b)*(p-c)))
