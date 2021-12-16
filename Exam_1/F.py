gl = {'a', 'e', 'i', 'o', 'u'}


def count_gl(s):
    res = 0
    for letter in s:
        if letter in gl:
            res += 1
    return res


n = int(input())
a = list()
for i in range(n):
    t = input()
    a.append(((-count_gl(t), len(t)), t))

a.sort(key=lambda k: k[0])

# print(*a)
for x in a:
    print(x[1])
