s1 = 'a'
s2 = 'b'


def fib(i):
    if i == 1:
        return s1
    elif i == 2:
        return s2
    else:
        return fib(i - 2) + fib(i - 1)


print(fib(int(input())))
