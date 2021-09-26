a, b, c, d, e, f = float(input()), float(input()), float(input()), \
                   float(input()), float(input()), float(input())
# x = (f - d * y) / c

det = a * d - c * b
det_y = a * f - e * c
det_x = e * d - f * b
x = det_x / det
y = det_y / det
print(x, y)
