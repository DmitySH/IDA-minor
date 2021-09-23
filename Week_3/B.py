from math import *

n = float(input())
if n - floor(n) < 0.5:
    print(floor(n))
else:
    print(ceil(n))
