import sys

f = sys.stdin

words = set()
for line in f:
    for word in line.split():
        words.add(word)
print(len(words))
