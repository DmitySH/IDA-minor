num1, num2 = int(input()), int(input())
if num1 > num2:
    max = num1
    second_max = num2
else:
    max = num2
    second_max = num1

while num2 != 0:
    num2 = int(input())
    if num2 != 0 and num2 > max:
        second_max = max
        max = num2
    elif num2 != 0 and num2 > second_max:
        second_max = num2

print(second_max)
