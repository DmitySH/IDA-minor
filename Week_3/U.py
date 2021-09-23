a, b, c, d, e, f = float(input()), float(input()), float(input()), \
                   float(input()), float(input()), float(input())
# x = (f - d * y) / c
# a * x + b * y = e
# a * (f - d * y) / c + b * y = e
# a * f / c - e = a * y * d / c - b * y
# a * f / c - e = y * (a * d / c - b)
# y = (a * f / c - e) / (a * d / c - b)

# y = (a * f / c - e) / (a * d / c - b)
# x = (f - d * y) / c

# print(x, y)

# y * (b - d) = e - f
det = a * d - c * b

if abs(det) >= 0.00000001:
    det_y = a * f - e * c
    det_x = e * d - f * b
    x = det_x / det
    y = det_y / det
    print(2, x, y)

elif a == b == c == d == e == f == 0:
    print(5)
elif a == c == 0:
    # y * (b - d) = e - f || x * (a - c) = e - f

    if b == d != 0:
        if e != f:
            print(0)
        else:
            print(f)
    elif b == d == 0:
        if e != 0 or d != 0:
            print(0)
        else:
            print(5)
    else:
        print(4, (e - f) / (b - d))
elif b == d == 0:
    if a == c != 0:
        if e != f:
            print(0)
        else:
            print(f)
    elif a == c == 0:
        if e != 0 or d != 0:
            print(0)
        else:
            print(5)
    else:
        print(3, (e - f) / (a - c))
elif a * d == b * c and a * f == c * e:
    if b != 0:
        print(1, -a / b, e / b)
    elif d != 0:
        print(1, -c / d, f / d)
