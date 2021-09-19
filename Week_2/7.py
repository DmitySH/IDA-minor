a, b, c = int(input()), int(input()), int(input())
if c < b:
    c, b = b, c
if c < a:
    a, c = c, a
if b < a:
    b, a = a, b
print(a, b, c)
