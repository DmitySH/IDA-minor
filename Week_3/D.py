p, x, y = float(input()), float(input()), float(input())
summ = x * 100 + y
summ += summ * (p / 100)
print(int(summ // 100), int(summ % 100))
