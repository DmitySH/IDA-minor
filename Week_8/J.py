inp = list(map(int, input().split()))
print(len(set(range(min(inp[0], inp[1]), max(inp[0], inp[1]) + 1)).
          intersection(
    set(range(min(inp[2], inp[3]), max(inp[2], inp[3]) + 1)))))
