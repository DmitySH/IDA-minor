a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

if a <= d and b <= e or a <= e and b <= d \
        or b <= d and c <= e or b <= e and c <= d \
        or a <= d and c <= e or a <= e and c <= d:
    print("YES")
else:
    print("NO")