import sys

print(len(set(sys.stdin.read().replace('\n', ' ').split())))
