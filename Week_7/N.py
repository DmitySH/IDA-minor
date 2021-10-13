def Intersection(a, b):
    f_index = 0
    s_index = 0
    res = list()
    while f_index < len(a) and s_index < len(b):
        if a[f_index] < b[s_index]:
            f_index += 1
        elif a[f_index] == b[s_index]:
            res.append(a[f_index])
            f_index += 1
            s_index += 1
        else:
            s_index += 1

    return res

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*Intersection(a, b))
