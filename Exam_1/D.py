def reverse(s):
    res = ''
    for h in s:
        res = h + res
    return res


def poly(s1):
    return reverse(s1) == s1


n = int(input())

ps = ''
a = list(input().split())
for x in a:
    ps += x

need = ''
for i in range(1, len(ps)):
    if poly(ps[:i] + ps[i:] + reverse(need)):
        break
    else:
        need = need + ps[i - 1]

if ps == reverse(ps):
    print(0)
    print()
else:
    print(len(need))
    print(*reverse(need))
