n = int(input())

print('+___ ' * n)
for i in range(n):
    print('|{} / '.format(i + 1), end='')
print()
print('|__\ ' * n)
print('|    ' * n)
