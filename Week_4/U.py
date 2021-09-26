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
    # det_y = a * f - e * c
    # det_x = e * d - f * b
    if a == 0 and c == 0 and abs(e / b - f / d) > 0.00001 or \
            b == 0 and d == 0 and abs(e / a - f / c) > 0.00001:
       print(0)
    elif a == 0 and c == 0 and abs(e / b - f / d) < 0.00001:
        print(3, e / b)
    elif b == 0 and d == 0 and abs(e / a - f / c) < 0.00001:
        print(4, e / a)
    elif abs(c * b / a - d) < 0.00001:
        print(1, -a / b, e / b)
    else:
        y = (f - c * e * 1 / a) / (c * b * 1 / a - d);
        x = (e - b * y) / a;
    print(2, x, y)
else:
    det_y = a * f - e * c
    det_x = e * d - f * b
    x = det_x / det
    y = det_y / det
    print(2, x, y)

